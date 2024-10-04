from rest_framework import serializers

from website.models import Product


class ProductSerializer(serializers.ModelSerializer):
    custom_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "custom_name",
            "created",
            "updated",
        ]

    def get_custom_name(self, obj: Product):
        return f"custom_{obj.name}"
