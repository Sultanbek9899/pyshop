from django.contrib import admin

# Register your models here.
from src.apps.product.models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "parent"]
    prepopulated_fields = {"slug": ("name",)}

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = [
        "title", "price", "category", 
        "stock_count", "updated_at", "created_at"
    ]
