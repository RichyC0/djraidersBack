from django.urls import path, include
from .views.role_views import *
from .views.user_views import *

urlpatterns = [
  path('register', registerUser, name = 'Register user')
]