from .models import Circuit, Constructor, Driver, Driverinseason, Grandprix, Raceresult

from django.contrib import admin

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    pass


@admin.register(Constructor)
class ConstructorAdmin(admin.ModelAdmin):
    pass
  
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
  
@admin.register(Driverinseason)
class DriverinseasonAdmin(admin.ModelAdmin):
    pass
  
@admin.register(Grandprix)
class GrandprixAdmin(admin.ModelAdmin):
    pass
  
@admin.register(Raceresult)
class RaceresultAdmin(admin.ModelAdmin):
    pass