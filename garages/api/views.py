from .serializers import GaragesSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from garages.models import RegisterGarage

class GaragesListCreate(ListCreateAPIView):
    serializer_class = GaragesSerializer
    queryset = RegisterGarage.objects.all()

class GaragesRetrieve(RetrieveUpdateDestroyAPIView):
    serializer_class = GaragesSerializer
    queryset = RegisterGarage.objects.all()

