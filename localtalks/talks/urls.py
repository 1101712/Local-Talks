from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdListView.as_view(), name='ad-list'),
    path('test/', views.test_view, name='test-view'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]