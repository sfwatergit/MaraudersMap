from rest_framework import serializers, pagination
from rest_framework.reverse import reverse
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from semantic_mapping.models import Building, Floor, Room


__all__ = [
    'RoomGeoSerializer',
    'PaginatedRoomGeoSerializer',
    'FloorGeoSerializer',
    'PaginatedFloorGeoSerializer',
    'BuildingGeoSerializer',
    'PaginatedBuildingGeoSerializer',
]


class RoomGeoSerializer(GeoFeatureModelSerializer):
    """A class to serialize locations as GEOJSON compatible data
    For example:
    """
    floor = serializers.RelatedField(source='floor.level')

    class Meta:
        model = Room
        fields = ('floor', 'room', 'geom')
        geo_field = 'geom'
        lookup_field = 'room'


class FloorGeoSerializer(GeoFeatureModelSerializer):
    building = serializers.RelatedField(source='building.name')
    rooms = RoomGeoSerializer(many=True)

    class Meta:
        model = Floor
        fields = ('building', 'level', 'geom', 'rooms', )
        geo_field = 'geom'


class BuildingGeoSerializer(GeoFeatureModelSerializer):
    floors = serializers.SerializerMethodField('get_building_floors')

    def get_building_floors(self, obj):
        return reverse('api_buildingfloor-list', args=[obj.name],
                       request=self.context['request'])

    class Meta:
        model = Building
        fields = ('name', 'street', 'postal_code', 'city', 'geom', 'floors')
        geo_field = 'geom'
        lookup_field = 'name'


class PaginatedBuildingGeoSerializer(pagination.PaginationSerializer):

    class Meta:
        object_serializer_class = BuildingGeoSerializer


class PaginatedFloorGeoSerializer(pagination.PaginationSerializer):

    class Meta:
        object_serializer_class = FloorGeoSerializer


class PaginatedRoomGeoSerializer(pagination.PaginationSerializer):

    class Meta:
        object_serializer_class = RoomGeoSerializer