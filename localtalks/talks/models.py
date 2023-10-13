from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete, pre_save
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


# Model representing user profile with extended fields
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True
    )
    using_default_image = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        try:
            this_old = CustomUser.objects.get(id=self.id)
            if this_old.profile_picture != self.profile_picture:
                this_old.profile_picture.delete(save=False)
        except CustomUser.DoesNotExist:
            pass  # object's been created - not exist in database

        super().save(*args, **kwargs)  # First call the original save method

        # Check if there is an image to resize
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)

            if img.height > 100 or img.width > 100:
                output_size = (100, 100)
                img.thumbnail(output_size)  # Resize the image
                img.save(self.profile_picture.path)
        else:
            print('No profile picture to resize.')


# Signal to delete old profile image when a new one is uploaded
@receiver(pre_save, sender=CustomUser)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:  # Check if the user instance exists (i.e., not a new user)
        try:
            old_image = CustomUser.objects.get(pk=instance.pk).profile_picture
            new_image = instance.profile_picture
            if old_image != new_image:
                old_image.delete(save=False)
        except CustomUser.DoesNotExist:
            pass  # User does not exist, likely a new user, so pass


# UserProfile model to extend user properties
class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
        )  # One-to-one relationship with CustomUser model

    # addition profile fields
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# Model representing individual advertisements
class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        CustomUser, related_name='ads', on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True)
    using_default_image = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # new save method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # first original save

        # Check the image for resize
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 200 or img.width > 200:
                output_size = (200, 200)
                img.thumbnail(output_size)
                img.save(self.image.path)

        else:
            print('No image to resize.')


# Model representing comments on advertisements
class Comment(models.Model):
    ad = models.ForeignKey(
        Ad, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]


# Signal to create or update UserProfile after CustomUser is saved
@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


# Signal to delete the ad image when an Ad instance is deleted
@receiver(post_delete, sender=Ad)
def delete_ad_image(sender, instance, **kwargs):
    if not instance.using_default_image:
        instance.image.delete(False)


# Signal to delete user and ad images when a CustomUser instance is deleted
@receiver(post_delete, sender=get_user_model())
def delete_user_images(sender, instance, **kwargs):
    if not instance.using_default_image:
        instance.profile_picture.delete(False)
    for ad in instance.ads.all():
        if not ad.using_default_image:
            ad.image.delete(False)
