from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Ad
from django.http import HttpResponse
from django.contrib import messages


class AdListView(ListView):
    model = Ad
    template_name = 'talks/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 10

def test_view(request):
    return HttpResponse("Test Page")

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ad-list')  # Redirect to the list of ads after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'talks/registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ad-list')  # Redirect to the list of ads after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'talks/registration/login.html', {'form': form})