from rest_framework import serializers

from src.apps.product.models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductListSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = CategorySerializer()

    class Meta: 
        model = Product
        fields = "__all__"
