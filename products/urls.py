from django.urls import path

from products.views import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductRetrieveAPIView,
    ProductDeleteAPIView,
)

urlpatterns = [
    path("list/", ProductListAPIView.as_view(), name="product_list"),
    path("create/", ProductCreateAPIView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateAPIView.as_view(), name="product_update"),
    path(
        "retrieve/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_retrieve"
    ),
    path("delete/<int:pk>/", ProductDeleteAPIView.as_view(), name="product_delete"),
]
