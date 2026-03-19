from django.contrib.gis.admin import GISModelAdmin
from .models import waterfall
from .models import caves
from .models import hill
from .models import spring
from django.contrib import admin

@admin.register(waterfall)
class waterfallAdmin(GISModelAdmin):
    list_display = ('name', 'address','location')

@admin.register(caves)
class caveAdmin(GISModelAdmin):
    list_display = ('name', 'address','location')

@admin.register(hill)
class hillAdmin(GISModelAdmin):
    list_display = ('name', 'address','location')

@admin.register(spring)
class springAdmin(GISModelAdmin):
    list_display = ('name', 'address','location')

     