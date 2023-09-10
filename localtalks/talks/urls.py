from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdListView.as_view(), name='ad-list'),  # List of all ads
    path('test/', views.test_view, name='test-view'),  # Test page
    path('register/', views.register_view, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('ad/<int:pk>/comment/', views.add_comment, name='add_comment'),  # Adding a comment to an ad
    path('ad/<int:ad_id>/', views.ad_detail, name='ad-detail'),  # Detailed ad page
]