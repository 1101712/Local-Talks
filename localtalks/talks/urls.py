from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    AdListView, AdDetailView, CustomLoginView, RegisterView,
    AdCreateView, test_view, HomeView, AdUpdateView,
    AdDeleteView, ProfileView, ProfileDeleteView, CommentDeleteView
)
from . import views
from django.contrib.auth import views as auth_views

# Define the URL patterns for the application
urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Homepage with latest ads
    path('ads/', AdListView.as_view(), name='ad-list'),  # List of all ads
    path('test/', test_view, name='test-view'),  # Test page
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('ad/create/', AdCreateView.as_view(), name='ad_create'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile_view'),
    path('ad/<int:pk>/edit/', AdUpdateView.as_view(), name='ad_edit'),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('how-it-works/', views.RulesView.as_view(), name='rules'),
    path(
        'profile/edit/', views.ProfileEditView.as_view(),
        name='profile_edit'
    ),
    path(
        'profile/delete/', views.ProfileDeleteView.as_view(),
        name='profile_delete'
    ),
    path(
        'comment/<int:pk>/delete/', CommentDeleteView.as_view(),
        name='comment_delete'
    ),
    # Password reset related URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='talks/password/password_reset_form.html',
        email_template_name='talks/password/password_reset_email.html'
    ), name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    # Category related URLs
    path(
        'categories/',
        views.CategoryListView.as_view(),
        name='category_list'
    ),
    path(
        'category/<str:category_name>/',
        views.AdsByCategoryView.as_view(),
        name='ads_by_category'
        ),
]
