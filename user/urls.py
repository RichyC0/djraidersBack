from django.urls import path, include
from .views.user_views import *

urlpatterns = [
  path('register', registerUser, name = 'Register user'),
  path('register/client', registerClient, name = 'Register client'),
  path('all/', getAllUsers, name= 'Get all users'),
  path('update/<str:personId>', updatePerson, name= 'Update User'),
  path('get/<str:personId>', getUser, name = 'Get User'),
  path('auth/', include('user.auth_urls'))
]