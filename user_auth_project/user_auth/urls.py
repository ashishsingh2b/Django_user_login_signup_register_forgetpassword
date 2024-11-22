from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
       # Template URLs
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),  # Logout URL

]
