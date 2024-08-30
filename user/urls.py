from django.urls import path
from .views.role_views import *
from .views.user_views import *

urlpatterns = [
  path('register', registerUser, name = 'Register user'),
  path('register/client', registerClient, name = 'Register client'),
  path('all/', getAllUsers, name= 'Get all users')
]