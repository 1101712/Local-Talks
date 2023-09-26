from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from PIL import Image
import os
from django.contrib.auth import get_user_model


# Model representing categories of ads
class Category(models.Model):
    # Name of the category. Ensures each category has a unique name.
    name = models.CharField(max_length=255, unique=True)
    
    # Optional description for more details about the category.
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        # Returns the name of the category when the object is referenced.
        return self.name


# Model representing user profile with extended fields like nickname and profile_picture
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # First call the original save method

        # Check if there is an image to resize
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)  # Open the image

            if img.height > 100 or img.width > 100:  # If the height or width is greater than 100 pixels
                output_size = (100, 100)  # Set the output size
                img.thumbnail(output_size)  # Resize the image
                img.save(self.profile_picture.path)  # Save the changes

        else:
            print('No profile picture to resize.')

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    # Дополнительные поля для профиля пользователя
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Model representing individual advertisements
class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, related_name='ads', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    # Вот новый метод save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сначала вызовем оригинальный метод save

        # Проверим, есть ли изображение для ресайза
        if self.image:
            img = Image.open(self.image.path)  # Откроем изображение

            if img.height > 200 or img.width > 200:  # Если высота или ширина больше 200 пикселей
                output_size = (200, 200)  # Установим размеры для вывода
                img.thumbnail(output_size)  # Изменим размер изображения
                img.save(self.image.path)  # Сохраним изменения

        else:
            print('No image to resize.')


# Model representing comments on advertisements
class Comment(models.Model):
    ad = models.ForeignKey(Ad, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_delete, sender=Ad)
def delete_ad_image(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_delete, sender=get_user_model())  # Используйте модель пользователя, указанную в вашем проекте
def delete_user_images(sender, instance, **kwargs):
    instance.profile_picture.delete(False)  # 'profile_picture' — это имя поля изображения в вашей модели пользователя
    # Удаление всех изображений объявлений связанных с этим пользователем
    for ad in instance.ads.all():  # 'ads' — это имя обратной связи к модели объявлений
        ad.image.delete(False)