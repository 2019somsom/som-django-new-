# users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('main/', views.main_view, name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]