from .models import Circuit, Constructor, Driver, Driverinseason, Grandprix, Raceresult, Season

from rest_framework import serializers


class CircuitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Circuit
        # all fields
        fields = '__all__'
        
    
class ConstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Constructor
        # all fields
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        # all fields
        fields = '__all__'
        
class DriverinseasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driverinseason
        # all fields
        fields = '__all__'
        
class GrandprixSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Grandprix
      fields = '__all__'
      
class RaceresultSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Raceresult
      fields = '__all__'
    
  