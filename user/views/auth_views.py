from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers.token_serializer import TokenSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenSerializer