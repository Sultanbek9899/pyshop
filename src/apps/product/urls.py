from django.urls import path


from src.apps.product import views



urlpatterns = [
    path("", views.get_index_page, name="index"),
    path("create/product/", views.create_product, name="create_product"),


    path("product/list/", views.ProductListView.as_view(), name="product_list"),
    path("product/wishlist/", views.ProductWishlistView.as_view(), name="wishlist"),
    path("add/wishlist/<int:pk>/", views.add_to_wishlist, name="add_wishlist")
]
