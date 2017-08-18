from django.contrib import admin

# Register your models here.
from .models import (City, Flowobservatory, Forecast, Forecastingtime, Irrigationarea, Irrigationwaterdemand, Light, Location, 
Nextreservoirlights, Nextweekp,Peopleslivelihoodwater, Prewaterlevel, Prewaterstoragecapacity, Q90, Q95, Regionalwaterregime, Reservoir, 
Reservoirstate, Rulecurve, Simreservoirflow, Waterintakestructures, Watersupply)

admin.site.register(City)
admin.site.register(Flowobservatory)
admin.site.register(Forecast)
admin.site.register(Forecastingtime)
admin.site.register(Irrigationarea)
admin.site.register(Irrigationwaterdemand)
admin.site.register(Light)
admin.site.register(Location)
admin.site.register(Nextreservoirlights)
admin.site.register(Nextweekp)
admin.site.register(Peopleslivelihoodwater)
admin.site.register(Prewaterlevel)
admin.site.register(Prewaterstoragecapacity)
admin.site.register(Q90)
admin.site.register(Q95)
admin.site.register(Regionalwaterregime)
admin.site.register(Reservoir)
admin.site.register(Reservoirstate)
admin.site.register(Rulecurve)
admin.site.register(Simreservoirflow)
admin.site.register(Waterintakestructures)
admin.site.register(Watersupply)
