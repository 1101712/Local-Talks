from django.shortcuts import get_object_or_404, render, redirect
from django.views import View, generic
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad, Comment, Category
from django.http import HttpResponse
from .forms import CommentForm, AdForm, ExtendedUserCreationForm, ProfilePictureForm
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages


class RegisterView(CreateView):
    form_class = ExtendedUserCreationForm
    template_name = 'talks/registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        """
        Override the form_valid method to login the user after registration.
        """
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, 'Your account has been successfully created.')
        return response
    
class CustomLoginView(LoginView):
    """
    Custom login view using Django's built-in LoginView.
    Redirects authenticated users to the ad-list view.
    """
    template_name = 'talks/registration/login.html'
    redirect_authenticated_user = True

class AdListView(ListView):
    model = Ad
    template_name = 'talks/ad/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date_posted')
        search_term = self.request.GET.get('search', '')
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) | 
                Q(description__icontains=search_term)
            )
        return queryset

class AdDetailView(FormMixin, DetailView):
    """
    Display the details of an ad and allow users to add comments.
    Integrates form handling within a DetailView using FormMixin.
    """
    model = Ad
    template_name = 'talks/ad/ad_detail.html'
    context_object_name = 'ad'
    form_class = CommentForm

    def get_success_url(self):
        """
        Define the URL to redirect to on successful form submission.
        """
        return reverse('ad_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        """
        Inject the list of comments related to the current ad into the context.
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(ad=self.object)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed POST variables
        and then check if it's valid.
        """
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Save the comment instance to the database after associating it with the current ad and user.
        """
        comment = form.save(commit=False)
        comment.ad = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

def test_view(request):
    """
    Simple test view that returns a basic HttpResponse.
    """
    return HttpResponse("Test Page")

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'talks/ad/ad_create.html'
    success_url = reverse_lazy('ad-list')

    def form_valid(self, form):
        """
        Set the ad's author to the current user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class HomeView(ListView):
    model = Ad
    template_name = 'talks/home.html'
    context_object_name = 'latest_ads'
    queryset = Ad.objects.all().order_by('-date_posted')[:5]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProfileView(View):
    template_name = 'talks/registration/profile.html'

    def get(self, request):
        ads = Ad.objects.filter(author=request.user)
        form = ProfilePictureForm(instance=request.user)  # Инициализируем форму
        return render(request, self.template_name, {'ads': ads, 'form': form})

    def post(self, request):
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error updating your profile picture')
            return redirect('profile')

class DeleteProfileView(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        logout(request)
        user.delete()
        return redirect('home')
    def get(self, request, *args, **kwargs):
        return render(request, 'delete_profile.html')

class AdUpdateView(UpdateView):
    model = Ad
    fields = ['title', 'description', 'image']
    template_name = 'talks/ad/ad_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        old_instance = Ad.objects.get(id=self.object.id)
        new_instance = form.save(commit=False)
        
        if old_instance.image != new_instance.image:
            old_instance.image.delete(save=False)
                    
        messages.success(self.request, 'Ad updated successfully')
        return super().form_valid(form)

class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'talks/ad/ad_delete.html'
    success_url = reverse_lazy('profile')

class CategoryListView(ListView):
    model = Category
    template_name = 'talks/ad/category_list.html'
    context_object_name = 'categories'

class AdsByCategoryView(ListView):
    model = Ad
    template_name = 'talks/ad/ads_by_category.html'  # имя шаблона
    context_object_name = 'ads'

    def get_queryset(self):
        return Ad.objects.filter(categories__name=self.kwargs['category_name'])

class RulesView(View):
    def get(self, request):
        return render(request, 'talks/rules.html')