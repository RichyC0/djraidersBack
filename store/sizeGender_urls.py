from django.urls import path
from .views.sizeGender_views import *

urlpatterns = [
  path('all/', getAllSizeGenders , name='Get all Sizes Gender'),
  path('get/<int:id>', getById , name='Get Specific Size Gender'),
]