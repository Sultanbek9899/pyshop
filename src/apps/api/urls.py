from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from src.apps.product import views

schema_view = get_schema_view(
    openapi.Info(
        title="FoodTales Api",
        default_version='v1',
        description="FoodTalesApi",
        contact=openapi.Contact(email="sultanbek9899@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('docs/', schema_view.with_ui("swagger")),
    path("product/list/", views.ProductListAPIView.as_view()),
    path("product/<int:pk>/", views.ProductDetailAPIView.as_view()),

    # auth endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]