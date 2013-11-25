from rest_framework import generics

from models import *
from semantic_mapping.models import Building, Floor
from serializers.sem_loc import *




#GeoList
#GeoJSONList
#GeoDetails
#GeoJSONDetails

class BuildingDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Building
    lookup_field = 'name'
    serializer_class = BuildingGeoSerializer

building_details = BuildingDetails.as_view()

class BuildingList(generics.ListCreateAPIView):
    model = Building
    serializer_class = BuildingGeoSerializer

    pagination_serializer_class = PaginatedBuildingGeoSerializer
    paginate_by_param = 'limit'
    paginate_by = 40


building_list = BuildingList.as_view()


class FloorList(generics.ListCreateAPIView):
    model = Floor
    serializer_class = FloorGeoSerializer
    pagination_serializer_class = PaginatedFloorGeoSerializer
    paginate_by_param = 'limit'
    paginate_by = 40


floor_list = FloorList.as_view()


class FloorDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Floor
    serializer_class = FloorGeoSerializer
    lookup_field = 'level'
    lookup_url_kwarg = 'name'


floor_details = FloorDetails.as_view()




class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Room
    serializer_class = RoomGeoSerializer


room_details = BuildingDetails.as_view()


class RoomList(generics.ListCreateAPIView):
    model = Room
    serializer_class = RoomGeoSerializer
    pagination_serializer_class = PaginatedRoomGeoSerializer
    paginate_by_param = 'limit'
    paginate_by = 40


room_list = RoomList.as_view()
