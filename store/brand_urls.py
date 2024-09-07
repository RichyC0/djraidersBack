from django.urls import path
from .views.brand_views import *

urlpatterns = [
  path('all/', getAllBrands , name='Get all Brands'),
  path('get/<int:id>', getById , name='Get Specific Brand'),
]