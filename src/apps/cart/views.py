from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from src.apps.product.models import Product
from src.apps.cart.cart import Cart
# Create your views here.

class CartPage(TemplateView):
    template_name = "cart.html"


def add_product(request, pk):
    cart = Cart(request)
    product = Product.objects.get(pk=pk)
    cart.add(product)
    return redirect("cart_page")


def remove_product(request, pk):
    cart = Cart(request)
    product = Product.objects.get(pk=pk)
    cart.remove(product)
    return redirect("cart_page")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_page")