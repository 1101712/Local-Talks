# Django and other module imports
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View, generic
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad, Comment, Category, CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from .forms import (
    CommentForm, AdForm, ExtendedUserCreationForm, ProfilePictureForm
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.core.files import File
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.forms import Form
from django import forms


# Class-based view for user registration
class RegisterView(CreateView):
    form_class = ExtendedUserCreationForm
    template_name = 'talks/registration/register.html'
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        """
        Override the form_valid method to login the user after registration,
        sets a default profile picture for the user and logs them in.
        """

        # Define paths and filenames for the default profile picture
        base_media_path = settings.MEDIA_ROOT
        default_image_folder = "default"
        default_image_filename = "default.jpg"

        # Call the parent class's form_valid method and get the user object
        response = super().form_valid(form)
        user = self.object
        # Check if a profile picture is set; if not, set a default one
        if not user.profile_picture:
            user.profile_picture.save(
                'default.jpg',
                File(
                    open(
                        os.path.join(
                            base_media_path,
                            default_image_folder,
                            default_image_filename
                        ),
                        'rb'
                    )
                )
            )
            user.using_default_image = True
            user.save()
        login(self.request, user)  # autho login
        return response


# Class-based view for custom login page
class CustomLoginView(LoginView):
    """
    Custom login view using Django's built-in LoginView.
    Redirects authenticated users to the ad-list view.
    """
    template_name = 'talks/registration/login.html'
    redirect_authenticated_user = True


# Function for hihliting a text by search
def highlight_text(text, query):
    start = text.lower().find(query.lower())
    if start == -1:
        return text
    end = start + len(query)
    return (text[:start] + "<strong>" + text[start:end] + "</strong>" +
            text[end:])


# Class-based view for listing ads
class AdListView(ListView):
    """
    Lists all ads with pagination and search functionality.
    """
    model = Ad
    template_name = 'talks/ad/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """
        Extends the default context data.
        Adds categories and media URL to the context for template rendering.
        Handles pagination logic.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['MEDIA_URL'] = settings.MEDIA_URL

        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page', 1)

        try:
            page = max(1, int(page))
        except ValueError:
            page = 1

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        search_query = self.request.GET.get('search', '')
        context['search_query'] = search_query

        # add function highlight_text for every ad
        if search_query:
            for ad in ads:
                ad.title = highlight_text(ad.title, search_query)
                ad.description = highlight_text(ad.description, search_query)
                ad.highlighted_categories = [
                    highlight_text(category.name, search_query)
                    for category in ad.categories.all()
                ]

        context['ads'] = ads

        return context

    def get_queryset(self):
        """
        Extends the default query set to add ordering and search functionality.
        Returns a filtered queryset based on the search term, if provided.
        """
        queryset = super().get_queryset().order_by('-date_posted')
        search_term = self.request.GET.get('search', '')
        author = self.request.GET.get('author', '')
        category = self.request.GET.get('category', '')
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(author__username__icontains=search_term) |
                Q(categories__name__icontains=search_term)

            )
        return queryset


# Class-based view for displaying ad details and comments
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
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the
        passed POST variables and then check if it's valid.
        """
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Save the comment instance to the database after associating it
        with the current ad and user.
        """
        comment = form.save(commit=False)
        comment.ad = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)


# Simple test view
def test_view(request):
    """
    Simple test view that returns a basic HttpResponse.
    """
    return HttpResponse("Test Page")


# Class-based view for the home page, shows the latest 6 ads
class HomeView(ListView):
    model = Ad
    template_name = 'talks/home.html'
    context_object_name = 'latest_ads'
    queryset = Ad.objects.all().order_by('-date_posted')[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


# Class-based view for the user's profile page
class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Displays the logged-in user's profile along with their ads.
    """
    template_name = 'talks/registration/profile_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = (Ad.objects.filter(author=self.request.user)
                                    .order_by('-date_posted'))
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


# Class-based view for editing the user's profile
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'talks/registration/profile_edit.html'
    fields = ['email', 'profile_picture']

    default_image_folder = 'default_images'
    default_image_filename = 'default.jpg'
    base_media_path = os.path.join(settings.MEDIA_ROOT)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile_view')

    def form_valid(self, form):
        user = self.request.user

        if user.profile_picture:
            user.using_default_image = False
        else:
            user.using_default_image = True

        user.save()

        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)


# Class-based view for deleting the user's profile
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'talks/registration/profile_delete.html'
    form_class = forms.Form
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been deleted.')
        return super().form_valid(form)


# Class-based view for creating a new ad
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
        base_media_path = settings.MEDIA_ROOT
        default_image_folder = "default"
        default_image_filename = "default.jpg"
        response = super().form_valid(form)
        ad = self.object
        if not ad.image:
            ad.image.save(
                'default.jpg',
                File(
                    open(
                        os.path.join(
                            base_media_path,
                            default_image_folder,
                            default_image_filename
                        ),
                        'rb'
                    )
                )
            )
            ad.using_default_image = True
            ad.save()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


# Class-based view for updating an existing ad
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['title', 'description', 'image']
    template_name = 'talks/ad/ad_edit.html'

    default_image_folder = 'default'
    default_image_filename = 'default.jpg'
    base_media_path = os.path.join(settings.MEDIA_ROOT)

    def get_success_url(self):
        return reverse_lazy('profile_view')

    def form_valid(self, form):
        old_instance = Ad.objects.get(id=self.object.id)
        new_instance = form.save(commit=False)

        if old_instance.image != new_instance.image:
            old_instance.image.delete(save=False)

        messages.success(self.request, 'Ad updated successfully')
        return super().form_valid(form)


# Class-based view for deleting an existing ad
class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'talks/ad/ad_delete.html'
    form_class = forms.Form

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj

    def get_success_url(self):
        return reverse('profile_view')

    def form_valid(self, form):
        messages.success(self.request, 'Your ad was successfully deleted.')
        return super().form_valid(form)


# Class-based view for listing all categories
class CategoryListView(ListView):
    model = Category
    template_name = 'talks/ad/category_list.html'
    context_object_name = 'categories'


# Class-based view for displaying ads by category
class AdsByCategoryView(ListView):
    model = Ad
    template_name = 'talks/ad/ads_by_category.html'
    context_object_name = 'ads'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Ad.objects.filter(categories__name=category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs['category_name']
        return context


# Class-based view for displaying the rules of the site
class RulesView(View):
    def get(self, request):
        return render(request, 'talks/rules.html')


# Class-based view for deleting a comment
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'talks/ad/comment_confirm_delete.html'
    form_class = Form

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.author != self.request.user:
            raise Http404("You do not have permission to delete this comment.")
        return obj

    def get_success_url(self):
        return reverse('ad_detail', kwargs={'pk': self.object.ad.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Your comment has been deleted.')
        return super().form_valid(form)
