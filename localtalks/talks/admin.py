from django.contrib import admin
from .models import CustomUser, Category, Ad, Comment, UserProfile


# Custom admin view for CustomUser model
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_picture_url')


# Custom admin view for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


# Custom admin view for Ad model
class AdAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'author', 'date_posted', 'image_url'
    )


# Custom admin view for Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ad', 'author', 'text', 'created_date')


# Custom admin view for UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')


# Register models to be managed in the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
