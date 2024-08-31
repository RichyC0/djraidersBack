from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('role/', include('user.role_urls')),
    path('category/', include('store.category_urls')),
    path('product/', include('store.product_urls')),
]
