from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import AdListView, AdDetailView, CustomLoginView, RegisterView, AdCreateView, test_view, HomeView, DeleteProfileView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Homepage with latest ads
    path('ads/', AdListView.as_view(), name='ad-list'),  # List of all ads
    path('test/', test_view, name='test-view'),  # Test page
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('login/', CustomLoginView.as_view(), name='login'),  # User login
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),  # Detailed ad page
    path('ad/create/', AdCreateView.as_view(), name='ad-create'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('delete_profile/', views.DeleteProfileView.as_view(), name='delete_profile'),
]