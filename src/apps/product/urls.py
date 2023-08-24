from django.urls import path


from src.apps.product import views



urlpatterns = [
    path("", views.get_index_page, name="index"),
    path("cart/", views.get_cart, name="cart"),
    path("create/product/", views.create_product, name="create_product")
]