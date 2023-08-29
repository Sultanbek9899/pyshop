from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from src.apps.product.models import Product, ProductImage, Category
from src.apps.product.serializers import ProductListSerializer
from src.apps.product.filters import ProductFilter

class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()



#

from src.apps.product.forms import CreateProductForm


def get_index_page(request):
    return render(request, "index.html")


def create_product(request):
    if request.method == "POST":
        print(request.POST)
        form = CreateProductForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            context={
                "form":form
            }
    else:
        form = CreateProductForm()
        context = {
            "form": form
        }
    return render(request, "create_product.html", context=context)


class ProductListView(FilterView):
    template_name="product_list.html"
    model = Product
    queryset = Product.objects.all()
    context_object_name = "products"
    filterset_class = ProductFilter




class ProductWishlistView(LoginRequiredMixin, ListView):
    template_name = "favorite.html"
    model = Product
    
    context_object_name = "products"
    # queryset = Pr


    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        wishlist = user.wishlist.all()
        return wishlist


@login_required
def add_to_wishlist(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    user.wishlist.add(product)
    return redirect("wishlist")
