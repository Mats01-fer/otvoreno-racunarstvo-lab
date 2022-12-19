
from django.shortcuts import render
from rest_framework import viewsets, generics
from django.views.generic import TemplateView
import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework import status


from rest_framework.views import APIView

from .models import Circuit, Constructor, Driver, Driverinseason, Grandprix, Raceresult
from .serializers import CircuitSerializer, ConstructorSerializer, DriverSerializer, DriverinseasonSerializer, GrandprixSerializer, RaceresultSerializer


def circuit(request):
    return render(request, 'circuit.html')

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'datatable.html')

class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    
class CircuitViewDetail(generics.RetrieveAPIView):
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
    
class CircuitsList(generics.ListAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'country', 'city', 'circuit_ref', ]
    
    

class ResultDetailApiView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieves the Raceresult with given id
        '''
        try:
            result = Raceresult.objects.get(id=pk)
            return Response(RaceresultSerializer(result).data)
        except Raceresult.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
class CircuitDetailApiView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieves the Circuit with given id
        '''
        try:
            circuit = Circuit.objects.get(id=pk)
            return Response(CircuitSerializer(circuit).data)
        except Circuit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class ConstructorViewSet(viewsets.ModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    
class ContructorDetailApiView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieves the Constructor with given id
        '''
        try:
            constructor = Constructor.objects.get(id=pk)
            return Response(ConstructorSerializer(constructor).data)
        except Constructor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
class DriverDetailApiView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        
        # if pk is not a number retun does not exist
        if(pk.isdigit() == False):
            return Response(status=status.HTTP_404_NOT_FOUND)
        '''
        Retrieves the Driver with given id
        '''
        try:
            driver = Driver.objects.get(id=pk)
            return Response(DriverSerializer(driver).data)
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, *args, **kwargs):
        '''
        Updates the Driver with given id
        '''
        try:
            driver = Driver.objects.get(id=pk)
            serializer = DriverSerializer(driver, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk, *args, **kwargs):
        driver = Driver.objects.get(id=pk)
        if driver:
            driver.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
            