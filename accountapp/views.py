# for token
from .serializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#for login view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyUser
from .serializer import MyUserSerializer 

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class MyUserLoginView():
    pass




