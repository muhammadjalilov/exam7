from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from task3.models import Product
from task3.serializers import ProductSerializer




class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




