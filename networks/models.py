from django.db import models


class Network(models.Model):
    NETWORK_TYPE_CHOICES = [
        ("factory", "Завод"),
        ("retail_network", "Розничная сеть"),
        ("individual_entrepreneur", "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=255, unique=True, verbose_name="название сети")
    network_type = models.CharField(
        max_length=50, choices=NETWORK_TYPE_CHOICES, verbose_name="тип сети"
    )
    email = models.EmailField(verbose_name="электронная почта")
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house_number = models.CharField(max_length=10, verbose_name="номер дома/здания")
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="поставщик",
    )
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="задолженность"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сеть"
        verbose_name_plural = "сети"

    @property
    def level(self):
        """
        Определяет уровень иерархии звена в сети. Завод имеет уровень 0,
        следующий за ним поставщик имеет уровень 1, и так далее.
        """
        if self.supplier is None:
            return 0
        else:
            return self.supplier.level + 1
