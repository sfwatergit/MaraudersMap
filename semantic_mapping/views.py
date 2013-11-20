from django.shortcuts import render

from rest_framework import generics

from models import *
from serializers.sem_loc import *
from serializers.filters import *

class GeojsonBuildingList(generics.ListCreateAPIView):
    model = Building
    serializer_class = BuildingGeoFeatureSerializer
    pagination_serializer_class = PaginatedBuildingGeoFeatureSerializer
    paginate_by_param = 'limit'
    paginate_by = 40

geojson_location_list = GeojsonBuildingList.as_view()
