from rest_framework import serializers
from .models import Mechanics


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanics
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'service_name',
        ]
