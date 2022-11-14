from django.shortcuts import render
from rest_framework import viewsets, generics
from django.views.generic import TemplateView
import django_filters.rest_framework


from .models import Circuit, Constructor, Driver, Driverinseason, Grandprix, Raceresult
from .serializers import CircuitSerializer, ConstructorSerializer, DriverSerializer, DriverinseasonSerializer, GrandprixSerializer, RaceresultSerializer


def circuit(request):
    return render(request, 'circuit.html')


def result(request):
    return render(request, 'datatable.html')

class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Raceresult.objects.all()
    serializer_class = RaceresultSerializer
    
    
class ResultsList(generics.ListAPIView):
    queryset = Raceresult.objects.all()
    serializer_class = RaceresultSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['year', 'driver', 'driver_number', ]

    # def get_queryset(self):
    #     queryset = Raceresult.objects.all()
    #     year = self.request.query_params.get('year')
    #     if year is not None:
    #         queryset = queryset.filter(year=year)
    #     return queryset