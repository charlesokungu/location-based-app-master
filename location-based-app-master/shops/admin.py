from django.contrib.gis.admin import OSMGeoAdmin
from .models import waterfall
from .models import caves
from .models import hill
from .models import spring
from django.contrib import admin

@admin.register(waterfall)
class waterfallAdmin(OSMGeoAdmin):
    list_display = ('name', 'address','location')

@admin.register(caves)
class caveAdmin(OSMGeoAdmin):
    list_display = ('name', 'address','location')

@admin.register(hill)
class hillAdmin(OSMGeoAdmin):
    list_display = ('name', 'address','location')

@admin.register(spring)
class springAdmin(OSMGeoAdmin):
    list_display = ('name', 'address','location')

     