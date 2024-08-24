from django.urls import path

from networks.views import (
    NetworkListAPIView,
    NetworkUpdateAPIView,
    NetworkRetrieveAPIView,
    NetworkDeleteAPIView,
    NetworkCreateAPIView,
)

urlpatterns = [
    path("list/", NetworkListAPIView.as_view(), name="network_list"),
    path("create/", NetworkCreateAPIView.as_view(), name="network_create"),
    path("update/<int:pk>/", NetworkUpdateAPIView.as_view(), name="network_update"),
    path(
        "retrieve/<int:pk>/", NetworkRetrieveAPIView.as_view(), name="network_retrieve"
    ),
    path("delete/<int:pk>/", NetworkDeleteAPIView.as_view(), name="network_delete"),
]
