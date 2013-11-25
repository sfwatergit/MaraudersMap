from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from marmap_users.models import  MobUserStatus, LocationFix
import semantic_mapping


class MobUserStatusSerializer(serializers.HyperlinkedModelSerializer):
    """Return all users
    """
    user = serializers.HyperlinkedIdentityField(view_name='user_status-detail')
    location_fix = serializers.HyperlinkedRelatedField(lookup_field='location_of', view_name='location-details')

    status_of = serializers.HyperlinkedRelatedField(lookup_field='user_status',
                                                    view_name='user_profile-details')


    class Meta:
        model = MobUserStatus

class MobUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """The profile of the User
    """
    user_status=serializers.HyperlinkedRelatedField(lookup_field='status_of',
                                                    view_name='user-status-details')
    users = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username',
        many=True,
        read_only=True
    )


#class MobUserStatusSerializer(serializers.HyperlinkedModelSerializer):
#    """
#    Use a nested relationship for the mobile users.
#    """
#    url = serializers.HyperlinkedIdentityField(
#        view_name='api_user_status',
#        lookup_field='uuid'
#    )
#    profile = MobUserProfileSerializer
#
#    class Meta:
#        model = MobUserStatus
#        fields = ('uuid',)

class FloorUserSerializer(serializers.HyperlinkedModelSerializer):
    floor = serializers.HyperlinkedIdentityField(view_name='floor_user-detail')

    class Meta:
        model = LocationFix

class BuildingUserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='building_user-detail', lookup_field='uuid')

    class Meta:
        model = LocationFix

class LocationFixSerializer(serializers.HyperlinkedModelSerializer):
    """

    {
     "device": {
     "uuid": "1d352410-4a5e-11e3-8f96-0800200c9a66"
      },
    "   epoch": 1384125523375
    },
        "semloc": {
        "uuid: "1243588493984390298dfna"
        "country": "US",
        "state": "CA",
        "city": "Berkeley",
        "street": "Leroy Ave",
        "building": "Soda Hall",
        "floor": "Floor 4",
        "room": "494"
        "strategy = 'SMT'
  },
    """

    class Meta:
        building = serializers.SlugRelatedField(slug_field='floors')
        model = LocationFix
        uuid = serializers.HyperlinkedIdentityField(view_name='locationfix-detail')
        #floor = serializers.HyperlinkedRelatedField(view_name='semantic_mapping.views.api_floor_list',
        #                                            lookup_field='floor')
        fields = ('uuid', 'location_of', 'country', 'state', 'city', 'street', 'building', 'floor', 'room', 'strategy')
        location_of = serializers.HyperlinkedRelatedField(lookup_field='location_of', view_name='mobuserstatus-detail')

#TODO: Remove
class LocationFixListSerializer(serializers.HyperlinkedModelSerializer):
    """

    {
     "device": {
     "uuid": "1d352410-4a5e-11e3-8f96-0800200c9a66"
      },
    "   epoch": 1384125523375
    },
        "semloc": {
        "uuid: "1243588493984390298dfna"
        "country": "US",
        "state": "CA",
        "city": "Berkeley",
        "street": "Leroy Ave",
        "building": "Soda Hall",
        "floor": "Floor 4",
        "room": "494"
        "strategy = 'SMT'
  },
    """

    class Meta:
        building = serializers.SlugRelatedField(slug_field='floors')
        model = LocationFix
        uuid = serializers.HyperlinkedIdentityField(view_name='locationfix-detail')
        #floor = serializers.HyperlinkedRelatedField(view_name='semantic_mapping.views.api_floor_list',
        #                                            lookup_field='floor')
        fields = ('uuid', 'room',)
        location_of = serializers.HyperlinkedRelatedField(lookup_field='location_of', view_name='mobuserstatus-detail')