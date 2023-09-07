from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdListView.as_view(), name='ad-list'),
    path('test/', views.test_view, name='test-view'),
]