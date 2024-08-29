from django.urls import path
from .views.role_views import *
from .views.user_views import *

urlpatterns = [
  path('role/all/', getAllRoles , name='Get all roles'),
  path('register', registerUser, name = 'Register user')
]