from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('role/', include('user.role_urls')),
    path('product/', include('store.product_urls')),
    path('category/', include('store.category_urls')),
    path('brand/', include('store.brand_urls')),
    path('sizeGender/', include('store.sizeGender_urls')),
    path('size/', include('store.size_urls')),
    path('sizeType/', include('store.sizeType_urls')),
    path('image/', include('store.image_urls')),
    path('auth/', include('user.auth_urls'))
]
