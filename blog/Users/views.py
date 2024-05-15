from django.shortcuts import render
from .serializers import TokenObtainSer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSer
