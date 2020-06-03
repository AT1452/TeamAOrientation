from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DonorSerializer
from .models import Donor

# Create your views here.

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all().order_by('name')
    serializer_class = DonorSerializer
