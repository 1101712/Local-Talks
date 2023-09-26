from django.contrib import admin
from .models import CustomUser, Category, Ad, Comment, UserProfile

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_picture')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'date_posted', 'image')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('ad', 'author', 'text', 'created_date')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)