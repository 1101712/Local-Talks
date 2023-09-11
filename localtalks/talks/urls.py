from django.urls import path
from .views import AdListView, AdDetailView, CustomLoginView, RegisterView, AdCreateView, test_view

urlpatterns = [
    path('', AdListView.as_view(), name='ad-list'),  # List of all ads
    path('test/', test_view, name='test-view'),  # Test page
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('login/', CustomLoginView.as_view(), name='login'),  # User login
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),  # Detailed ad page
    path('ad/create/', AdCreateView.as_view(), name='ad-create'),
]