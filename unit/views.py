from rest_framework import generics
from .models import Unit
from .serializers import UnitSerializer

class UnitList(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
