from .models import Circuit, Constructor, Driver, Driverinseason, Grandprix, Raceresult

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
    # raceresult doesnt have a primary key, so we need to specify it
    # drivername = serializers.SerializerMethodField()


    # def get_drivername(self, result):
    #     # return ', '.join([str(genre) for genre in album.genres.all()])
    #     # driver = Driverinseason.objects.filter(driverid=result.driverid, year=result.year, constructorid=result.constructorid).first()
    #     # driverProper = Driver.objects.filter(id=driver.driverid_id)[0]
    
    #     return "janko jankic"
    
    class Meta:
      model = Raceresult
      fields = ('id', 'fastestlaptime', 'grid', 'position', 'laps', 'time', 'fastestlap', 'points', 'status', 'driverid', 'year', 'constructorid', 'gpid')
    
  