from rest_framework import serializers, pagination
from semantic_mapping.models import Building, Floor, Room
from semantic_mapping.serializers.geo_serializers import GeoModelSerializer


class RoomGeoSerializer(GeoModelSerializer):
    """A class to serialize locations as GEOJSON compatible data
    For example:
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='api_room_details', lookup_field='rooms')
    mob_users_in_room = serializers.SerializerMethodField('get_users_in_room')


    class Meta:
        model = Room
        fields = ('floor', 'room_number')
        exclude = ('poly',)
        geo_field = 'position'


class FloorGeoSerializer(GeoModelSerializer):
   # building = serializers.HyperlinkedRelatedField(lookup_field='name', view_name='api_building-details')
    #rooms = RoomGeoSerializer(many=True)
    #level = serializers.HyperlinkedIdentityField(
    #    view_name='api_floor-details', lookup_field='level')


    class Meta:
        model = Floor
        geo_field = 'position'
        fields = ('level', 'building', 'rooms',)


#Room Serializers:



class PaginatedRoomGeoSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = RoomGeoSerializer


#Building Serializers:
class BuildingGeoSerializer(GeoModelSerializer):

    #geometry = gis_serializers.GeometryField(required=True)

    name = serializers.HyperlinkedIdentityField(view_name='api_building-details',
                                                   lookup_field='name')
    floors = FloorGeoSerializer(many=True)

    class Meta:
        model = Building
        fields = ('name', 'street', 'postal_code', 'city', 'position','floors' )
        geo_field = 'position'


class PaginatedBuildingGeoSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = BuildingGeoSerializer


#Floor Serializers:


class PaginatedFloorGeoSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = FloorGeoSerializer
