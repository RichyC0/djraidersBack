from django.urls import path
from .views.product_views import *

urlpatterns = [
 path('all/', getAllProduct , name='Get all Products'),
 path('update/<str:categoryId>/<str:productId>', updateProduct, name='Update Product' ),
 path('register/<str:categoryId>', registerProduct, name='Register Product' ),
 path('all/category/<str:categoryId>', getAllByCategory ,name='Get All Products By Category' ),
 path('get/<str:id>', getById, name='Get Product By Id' )
]