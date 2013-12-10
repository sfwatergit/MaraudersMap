from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from marmap_users.models import LocationFix, MobUserStatus
from marmap_users.user_serializers import MobUserStatusSerializer, LocationSerializer, UserSerializer
import django_filters

class OnlineUserFilter(django_filters.FilterSet):
    class Meta:
        model = MobUserStatus
        fields=['location_fix', 'status', 'status_changed']


class LocationViewSet(viewsets.ModelViewSet):
    """

    """
    serializer_class = LocationSerializer
    queryset = LocationFix.objects.all()
    lookup_field = 'id'


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


userdetail = UserViewSet.as_view()


class MobUserStatusViewSet(viewsets.ModelViewSet):
    """
    Status of the mobile phone user.
    """
    serializer_class = MobUserStatusSerializer
    queryset = MobUserStatus.objects.all()
    lookup_field = 'id'
    filter_class = OnlineUserFilter


class LocationFixDetailView(generics.RetrieveUpdateAPIView):
    serializer = LocationSerializer
    lookup_field = 'id'
    queryset = LocationFix.objects.all()


locationfix = LocationFixDetailView.as_view()


class FloorUserViewSet(viewsets.ModelViewSet):
    model = LocationFix
    lookup_field = 'uuid'








