from mechanics.models import Mechanics
from rest_framework import serializers


class MechanicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanics
        fields = [
            "first_name",
            "username",
            "email",
            "password",
            "service_name",
        ]
