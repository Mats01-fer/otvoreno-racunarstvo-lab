from .models import Circuit, Constructor, Driver, Driverinseason, Grandprix, Raceresult

from rest_framework import serializers


class CircuitSerializer(serializers.ModelSerializer):


    context = serializers.SerializerMethodField()
    
    def get_context(self, circuit):
        return {
            "@context": "http://schema.org",
            "@type": "Circuit",
            "name": "given name",
            "location": "https://schema.org/address",
            "country": "https://schema.org/addressCountry",
            "lat": "https://schema.org/latitude",
            "lon": "https://schema.org/longitude",
            "url": "https://schema.org/url",
            "alt": "https://schema.org/elevation"
        }

    class Meta:
        model = Circuit
    
        ## add JSON-LD context

        fields = ('id', 'name', 'location', 'country', 'lat', 'lon', 'context')
        
        
        
    
class ConstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Constructor
        # all fields
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    
    
    context = serializers.SerializerMethodField()
    
    def get_context(self, circuit):
        return {
            "@context": "http://schema.org",
            "@type": "Person",
            "name": "given name",
            "surname": "family name",
            "code": "https://schema.org/identifier",
            "dob": "https://schema.org/birthDate",
            "nationality": "https://schema.org/national",
            "id": "https://schema.org/identifier"
        }

    class Meta:
        model = Driver
        # all fields
        fields = ('name','surname','code','dob','nationality','id', 'context')
        
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
    
    driver = serializers.SerializerMethodField()
    driver_number = serializers.SerializerMethodField()
    constructor = serializers.SerializerMethodField()
    circuit = serializers.SerializerMethodField()
    grand_prix = serializers.SerializerMethodField()
    
    def get_constructor(self, result):
        constructor = Constructor.objects.filter(id=result.constructorid).first()
        return constructor.name
    
    def get_circuit(self, result):
        gp = Grandprix.objects.filter(id=result.gpid_id).first()
        circuit = Circuit.objects.filter(id=gp.circuitid_id).first()
        return circuit.name
    
    def get_grand_prix(self, result):
        gp = Grandprix.objects.filter(id=result.gpid_id).first()
        return gp.name
    
    def get_driver(self, result):

        driver = Driver.objects.filter(id=result.driverid_id).first()
        return driver.name + " " + driver.surname 
    def get_driver_number(self, result):
        driverinseason = Driverinseason.objects.filter(year=result.year, driverid_id=result.driverid_id).first()
        return driverinseason.number 
    
    class Meta:
      model = Raceresult
      fields = ('id', 'driver', 'driver_number', 'constructor', 'circuit', 'grand_prix','fastestlaptime', 'grid', 'position', 'laps', 'time', 'fastestlap', 'points', 'status', 'driverid', 'year', 'constructorid', 'gpid')
    
  