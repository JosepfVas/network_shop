from rest_framework.serializers import ModelSerializer
from networks.models import Network


class NetworkSerializer(ModelSerializer):
    """Сериализатор сети"""

    class Meta:
        model = Network
        fields = [
            "name",
            "network_type",
            "email",
            "city",
            "country",
            "street",
            "house_number",
            "supplier",
            "created_at",
            "debt",
        ]
        read_only_fields = ["debt"]
