from rest_framework import serializers
from garages.models import RegisterGarage

class GaragesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterGarage
        fields = (
            "id",
            "garage_name",
            "garage_location",
            "garage_email",
            "garage_telephone",
        )



