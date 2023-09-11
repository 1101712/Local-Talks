from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment, Ad

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image']