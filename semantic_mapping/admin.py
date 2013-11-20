from django.contrib.gis import admin
from semantic_mapping.models import *


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'position', 'city', 'street', 'added_on', 'updated_on')


admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(MobUserProfile)
admin.site.register(MobUserState)
admin.site.register(LocationFix)
admin.site.register(LocationFixSource)
