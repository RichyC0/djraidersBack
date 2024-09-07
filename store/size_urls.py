from django.urls import path
from .views.size_view import *

urlpatterns = [
  path('all/<str:categoryId>', getAllBySizeType , name='Get all Sizes By Category'),
  path('get/<str:sizeTypeId>/<int:sizeId>', getById , name='Get Specific Size')
]