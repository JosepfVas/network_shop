from rest_framework import generics
from products.models import Product
from networks.paginators import CustomPaginator
from products.serializers import ProductSerializer


# CRUD для продуктов.
class ProductCreateAPIView(generics.CreateAPIView):
    """Создание продукта"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListAPIView(generics.ListAPIView):
    """Список всех продуктов"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPaginator


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одного продукта"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Обновление продукта"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDeleteAPIView(generics.DestroyAPIView):
    """Удаление продукта"""

    queryset = Product.objects.all()
