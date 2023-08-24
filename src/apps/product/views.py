from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

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



#

from src.apps.product.forms import CreateProductForm


def get_index_page(request):
    return render(request, "index.html")


def get_cart(request):
    return render(request, "cart.html")

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