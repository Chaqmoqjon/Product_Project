from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serialazers import PRODUCTSerializer
from .models import PRODUCT
from rest_framework import permissions

# Create your views here.
class PRODUCTViewSet(ModelViewSet):
    queryset = PRODUCT.objects.all()
    serializer_class = PRODUCTSerializer
    permission_classes = (permissions.AllowAny, )