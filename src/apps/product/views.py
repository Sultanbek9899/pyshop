from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from src.apps.product.models import Product, ProductImage, Category
from src.apps.product.serializers import ProductListSerializer

class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()