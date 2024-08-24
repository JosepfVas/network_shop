from django.db import models

from networks.models import Network


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="название продукта")
    model = models.CharField(max_length=255, verbose_name="модель продукта")
    release_date = models.DateField(verbose_name="дата выпуска")
    network = models.ForeignKey(
        Network,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="ссылка на сеть",
    )

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
