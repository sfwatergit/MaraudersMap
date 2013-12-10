from django.contrib.auth.models import User
from rest_framework import serializers
from marmap_users.models import MobUserStatus, LocationFix
import semantic_mapping


class MobUserStatusSerializer(serializers.HyperlinkedModelSerializer):
    """Return all users
    """
    username=serializers.RelatedField(source='user.username')


    class Meta:
        lookup_field = 'id'
        model = MobUserStatus
        fields = ('id', 'user', 'username',  'location_fix', 'status', 'status_changed')

class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User

        fields = ('url', 'status_of', 'username', 'first_name', 'last_name')
        #exclude = ('groups', 'user_permissions')
        lookup_field = 'id'





class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        lookup_field = 'id'
        model = LocationFix
        fields = ('url', 'uuid', 'epoch', 'country', 'state', 'city', 'street', 'building',
                  'floor',
                  'room',
                  'strategy',
       'of_user')






