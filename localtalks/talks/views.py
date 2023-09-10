from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Ad, Comment
from django.http import HttpResponse
from django.contrib import messages
from .forms import CommentForm


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

def save_comment(request, ad):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.ad = ad
        comment.author = request.user
        comment.save()
        return True, form
    return False, form

def add_comment(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == "POST":
        is_saved, form = save_comment(request, ad)
        if is_saved:
            return redirect('ad-detail', pk=ad.pk)
    else:
        form = CommentForm()
    return render(request, 'talks/add_comment.html', {'form': form})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    comments = Comment.objects.filter(ad=ad)
    
    if request.method == 'POST':
        is_saved, form = save_comment(request, ad)
        if is_saved:
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = CommentForm()

    return render(request, 'talks/ad_detail.html', {'ad': ad, 'comments': comments, 'form': form})