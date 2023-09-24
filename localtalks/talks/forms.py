from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Comment, Ad, CustomUser

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image']
        
class ExtendedUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=255, required=False, help_text='Optional.')
    profile_picture = forms.ImageField(required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'nickname', 'profile_picture')