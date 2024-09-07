from django.urls import path
from .views.sizeType_views import *

urlpatterns = [
  path('all/', getAll , name='Get all Size Type'),
  path('get/<int:id>', getById , name='Get Specific Size Types'),
]