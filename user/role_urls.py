from django.urls import path
from .views.role_views import *
from .views.user_views import *

urlpatterns = [
  path('all/', getAllRoles , name='Get all roles'),
  path('assign', assigRole , name='Assign role to user'),
]