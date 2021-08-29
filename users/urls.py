from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('user/<int:pk>/', views.public_profile, name='profile-detail-view'),   
]