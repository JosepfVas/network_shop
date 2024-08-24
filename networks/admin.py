from django.contrib import admin
from networks.models import Network


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "network_type",
        "city",
        "debt",
        "supplier",
        "supplier_link",
    )
    list_filter = ("city",)
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            return admin.utils.format_html(
                '<a href="{}">{}</a>',
                admin.utils.reverse(
                    "admin:networks_network_change", args=[obj.supplier.id]
                ),
                obj.supplier.name,
            )
        return "-"

    supplier_link.short_description = "Ссылка на поставщика"
