from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from .views.auth_views import CustomTokenObtainPairView

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='Obtain JWT Token'),
    path('token/refresh', TokenRefreshView.as_view(), name='Obtain JWT Token Refresh'),
]