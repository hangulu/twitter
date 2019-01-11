from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemeSerializer
from .models import Popmemes

# Create your views here.
class MemeView(viewsets.ModelViewSet):
  serializer_class = MemeSerializer
  queryset = Popmemes.objects.all()
