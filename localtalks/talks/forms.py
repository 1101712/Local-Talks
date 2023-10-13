from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Comment, Ad, CustomUser, Category
from django.core.exceptions import ValidationError
from django.db import models


# Form for creating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


# Form for creating and editing ads
class AdForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Ad
        fields = ['title', 'description', 'image', 'categories']


# Extended user creation form with email and optional profile picture
class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'password1', 'password2', 'profile_picture'
        )

    # Validate the uniqueness of the username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "A user with that username already exists."
            )
        return username
    # Validate the uniqueness of the email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "A user with that email already exists."
            )
        return email

# Form for updating the profile picture
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # same model as in ExtendedUserCreationForm
        fields = ['profile_picture']
