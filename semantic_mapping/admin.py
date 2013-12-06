from django.contrib.gis import admin
from MaraudersMap import settings
from semantic_mapping.models import *


GEODJANGO_IMPROVED_WIDGETS = 'olwidget' in settings.INSTALLED_APPS

if GEODJANGO_IMPROVED_WIDGETS:
    from olwidget.admin import GeoModelAdmin
else:
    from django.contrib.gis.admin import ModelAdmin as GeoModelAdmin


class BuildingAdmin(GeoModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'geom')

class FloorAdmin(GeoModelAdmin):
    list_display = ('building', 'level', 'rooms', 'geom')

class RoomAdmin(GeoModelAdmin):
    list_display = ('floor', 'room', 'geom')

admin.site.register(Building, BuildingAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Room, RoomAdmin)

