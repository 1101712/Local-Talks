from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Comment, Ad, CustomUser
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image']

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with that username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
