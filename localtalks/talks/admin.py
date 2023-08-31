from django.contrib import admin
from .models import UserProfile, Category, Ad, Comment

# Registering the UserProfile model to make it available in the admin panel.
admin.site.register(UserProfile)

# Registering the Category model to make it available in the admin panel.
admin.site.register(Category)

# Registering the Ad model to make it available in the admin panel.
admin.site.register(Ad)

# Registering the Comment model to make it available in the admin panel.
admin.site.register(Comment)