from django.urls import path


from src.apps.product import views

urlpatterns = [
    path("api/product/list/", views.ProductListAPIView.as_view()),
]