from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from networks.models import Network
from networks.paginators import CustomPaginator
from networks.serializers import NetworkSerializer


# CRUD для сетей.


class NetworkCreateAPIView(generics.CreateAPIView):
    """Создание сети"""

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworkListAPIView(generics.ListAPIView):
    """Список всех сетей"""

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country", "city"]
    pagination_class = CustomPaginator


class NetworkRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одной сети"""

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworkUpdateAPIView(generics.UpdateAPIView):
    """Обновление сети"""

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworkDeleteAPIView(generics.DestroyAPIView):
    """Удаление сети"""

    queryset = Network.objects.all()
