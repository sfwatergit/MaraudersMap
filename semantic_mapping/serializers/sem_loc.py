from rest_framework import serializers, pagination, generics
from django.contrib.auth.models import User
from semantic_mapping.models import Building
from semantic_mapping.serializers.filters import InBBOXFilter
from semantic_mapping.serializers.geo_serializers import GeoFeatureModelSerializer


class MobUserSerializer():
    """
    {
     "device": {
    "uuid": "1d352410-4a5e-11e3-8f96-0800200c9a66"
     },
    "epoch": 1384125523375
    }
    """


class LocalizationSerializer():
    """
    {
        "semloc": {
        "country": "US",
        "state": "CA",
        "city": "Berkeley",
        "street": "Leroy Ave",
        "building": "Soda Hall",
        "floor": "Floor 4",
        "room": "494"
  },
    """
class BuildingGeoFeatureSerializer(GeoFeatureModelSerializer):
    """A class to serialize locations as GEOJSON compatible data
    For example:
    """
    details = serializers.HyperlinkedIdentityField(
        view_name='api_geojson_building_details')
    fancy_name = serializers.SerializerMethodField('get_fancy_name')

    def get_fancy_name(self, obj):
        return u'You are in %s' % obj.name

    class Meta:
        model = Building
        geo_field = "position"


class PaginatedBuildingGeoFeatureSerializer(pagination.PaginationSerializer):

    class Meta:
        object_serializer_class = BuildingGeoFeatureSerializer


class GeojsonBuildingContainedInBBoxList(generics.ListAPIView):
    model = Building
    serializer_class = BuildingGeoFeatureSerializer
    queryset = Building.objects.all()
    bbox_filter_field = 'geometry'
    filter_backends = (InBBOXFilter,)

geojson_location_contained_in_bbox_list = GeojsonBuildingContainedInBBoxList.as_view()

class GeojsonBuildingOverlapsBBoxList(GeojsonBuildingContainedInBBoxList):
    bbox_filter_include_overlapping = True

geojson_location_overlaps_bbox_list = GeojsonBuildingOverlapsBBoxList.as_view()


class GeojsonBuildingDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Building
    serializer_class = BuildingGeoFeatureSerializer

geojson_location_details = GeojsonBuildingDetails.as_view()
