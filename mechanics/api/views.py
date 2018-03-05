from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, JsonResponse
from .serializers import MechanicSerializer
from mechanics.models import Mechanics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class MechanicsList(ListCreateAPIView):
    serializer_class = MechanicSerializer
    queryset = Mechanics.objects.all()


class MechanicsDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MechanicSerializer
    queryset = Mechanics.objects.all()








