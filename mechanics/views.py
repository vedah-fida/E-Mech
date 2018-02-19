from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Mechanics
from rest_framework import generics, viewsets
from .serializers import MechanicSerializer


# Create your views here.

@login_required(login_url='login:login_user')
def all_mechanics(request):
    all_mechanics = "<h3>The listing for all the mechanics</h3>"
    return HttpResponse(all_mechanics)


class MechanicsListingView(generics.ListAPIView):
    serializer_class = MechanicSerializer
    queryset = Mechanics.objects.all()


class MechanicsView(generics.ListCreateAPIView):
    serializer_class = MechanicSerializer
    queryset = Mechanics.objects.all()


class MechanicUpdateView(generics.UpdateAPIView):
    serializer_class = MechanicSerializer
    queryset = Mechanics.objects.all()
