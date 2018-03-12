from mechanics.models import Mechanics
from rest_framework.serializers import ModelSerializer

class MechanicSerializer(ModelSerializer):
    class Meta:
        model = Mechanics
        fields = (
            'first_name',
            'last_name',
            'email',
        )
