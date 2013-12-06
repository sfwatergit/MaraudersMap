from django.shortcuts import get_object_or_404
from rest_framework import generics
from marmap_users.mixins import MultipleFieldLookupMixin

from models import *
from semantic_mapping.models import Building, Floor
from serializers.map_serializer import *


#GeoList
#GeoJSONList
#GeoDetails
#GeoJSONDetails


class BuildingDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildingGeoSerializer
    queryset = Building.objects.all()
    lookup_url_kwarg = 'name'
    lookup_field = 'name'

building_details = BuildingDetails.as_view()


class FloorDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FloorGeoSerializer
    queryset = Building.objects.all()

    def get_object(self, queryset=queryset):
        queryset = self.get_queryset()
        name = self.kwargs['building']
        floor = self.kwargs['level']
        building = Building.objects.get(name=name)
        level = building.floors.get(level=floor)
        return level

floor_details = FloorDetails.as_view()

class BuildingFloors(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorGeoSerializer

    def get_queryset(self):
        building_name = self.kwargs['building']
        return self.queryset.filter(building__name=building_name)

    def pre_save(self, obj):
        obj.building_id = self.kwargs['building']

building_floors = BuildingFloors.as_view()


class BuildingFloorRooms(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorGeoSerializer

    def get_queryset(self):
        building_name = self.kwargs['building']
        floor_name = self.kwargs['level']
        return self.queryset.filter(building__name=building_name, building__name__floor=floor_name) 

    def pre_save(self, obj):
        obj.building_id = self.kwargs['building']

floorroom_list = BuildingFloors.as_view()


class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomGeoSerializer
    queryset = Building.objects.all()


    def get_object(self, queryset=queryset):
        queryset = self.get_queryset()
        name = self.kwargs['name']
        floor = self.kwargs['level']
        room = self.kwargs['room']
        building = Building.objects.get(name=name)
        level = building.floors.get(level=floor)
        room = level.rooms.get(room=room)
        return room


    def pre_save(self, obj):
        obj.building_id = self.kwargs['building']

room_details = RoomDetails.as_view()


class BuildingList(generics.ListCreateAPIView):
    model=Building
    serializer_class = BuildingGeoSerializer
    pagination_serializer_class = PaginatedBuildingGeoSerializer
    paginate_by_param = 'limit'
    paginate_by = 40
    lookup_field = 'name'


building_list = BuildingList.as_view()


class FloorList(generics.ListCreateAPIView):
    model = Floor
    serializer_class = FloorGeoSerializer
    pagination_serializer_class = PaginatedFloorGeoSerializer
    paginate_by_param = 'limit'
    paginate_by = 40
    lookup_fields = 'name'


floor_list = FloorList.as_view()


class RoomList(MultipleFieldLookupMixin, generics.ListCreateAPIView):
    model = Room
    serializer_class = RoomGeoSerializer
    pagination_serializer_class = PaginatedRoomGeoSerializer
    paginate_by_param = 'limit'
    paginate_by = 40
    lookup_fields = ('name', 'level')


room_list = RoomList.as_view()

