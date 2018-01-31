from mechanics.models import Mechanics
from rest_framework import generics


class MechanicCRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset = Mechanics.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Mechanics.objects.get(pk)
