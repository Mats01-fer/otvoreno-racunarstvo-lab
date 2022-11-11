from django.shortcuts import render
from rest_framework import viewsets
from .models import Circuit
from .serializers import CircuitSerializer


def index(request):
    return render(request, 'circuits.html')


class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer