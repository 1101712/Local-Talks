from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    nickname = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True)  # New field for ad images

    def __str__(self):
        return self.title


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