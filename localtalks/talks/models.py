from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from PIL import Image
import os
from django.contrib.auth import get_user_model
import cloudinary.uploader


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
    profile_picture_url = models.URLField(blank=True, null=True)
    using_default_image = models.BooleanField(default=True)

    def __str__(self):
        return self.username


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
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


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
