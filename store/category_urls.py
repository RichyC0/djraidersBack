from django.urls import path
from .views.category_views import *

urlpatterns = [
 path('all/', getAllCategories , name='Get all Categories'),
 path('register', registerCategories, name='Register Category' ),
 path('update/<str:id>', updateCategory, name='Update Category' ),
 path('get/<str:id>', getCategoryById, name='Get Category' )
]