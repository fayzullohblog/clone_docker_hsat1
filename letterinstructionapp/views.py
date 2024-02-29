from django.shortcuts import render
from .serializer import LetterTemplatesserializer
from rest_framework import generics
from .models import TinyNoSigned

# Create your views here.


class LetterTemplatesCreateApiView(generics.CreateAPIView):
    queryset=TinyNoSigned.objects.all()
    serializer_class=LetterTemplatesserializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


   
