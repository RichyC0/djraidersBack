
from django.urls import path
from .views.image_views import *

urlpatterns = [
  path('uploadFile', uploadFile, name='Subir imagenes'),
]