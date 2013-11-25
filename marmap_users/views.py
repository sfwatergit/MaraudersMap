from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import get_object_or_404
from django.utils.encoding import iri_to_uri, smart_text
from django.utils.text import slugify
from rest_framework import generics, viewsets
from rest_framework.decorators import link, action
from marmap_users.mixins import MultipleFieldLookupMixin
from marmap_users.models import LocationFix, MobUserStatus
from marmap_users.user_serializers import LocationFixListSerializer



#class MobUserViewList(generics.ListCreateAPIView):
#    model = MobUserProfile
#    serializer_class = MobUserProfileSerializer
#
#    def get_queryset(self):
#        floor_pk = self.kwargs.get('pk', None)
#        if floor_pk is not None:
#            return MobUserProfile.objects.filter(floor__pk=floor_pk)
#        return MobUserProfile.objects.all()
#
#class MobUserViewDetail(generics.ListCreateAPIView):
#    model = MobUserProfile
#    serializer_class = MobUserProfileSerializer
#
#    def get_queryset(self):
#        floor_pk = self.kwargs.get('pk', None)
#        if floor_pk is not None:
#            return MobUserProfile.objects.filter(floor__pk=floor_pk)
#        return MobUserProfile.objects.all()
#
#mobuserprofile_detail = MobUserViewDetail.as_view()



class LocationList(MultipleFieldLookupMixin, generics.ListAPIView):
    """
    View the Locations of users for selected floor
    """
    #model = LocationFix
    serializer_class = LocationFixListSerializer
    lookup_url_kwarg = ('building', 'level')
    lookup_fields = ('building', 'level')


    def get_queryset(self):
    #TODO: Fix this
        conn = connection
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT marmap_users_locationfix.uuid AS uuid, marmap_users_locationfix.room FROM public.marmap_users_locationfix, public.marmap_users_mobuserprofile, public.marmap_users_mobuserstatus, public.auth_user WHERE marmap_users_locationfix.uuid = marmap_users_mobuserstatus.location_fix_id AND marmap_users_mobuserprofile.user_status_id =marmap_users_mobuserstatus.id AND auth_user.id = marmap_users_mobuserprofile.user_id AND marmap_users_mobuserstatus.status = 'online' AND marmap_users_mobuserstatus.status_changed = True AND marmap_users_locationfix.building = %s AND marmap_users_locationfix.floor = %s;''',
            [self.kwargs['building'], self.kwargs['level']])
        user =  dictfetchall(cursor)

        return user

locationfix = LocationList.as_view()

class BuildingUserViewSet(viewsets.ModelViewSet):
    """

    """
    model = LocationFix
    lookup_field = 'building'

class FloorUserViewSet(viewsets.ModelViewSet):
    model = LocationFix
    lookup_field = 'floor'

class MobUserStatusViewSet(viewsets.ModelViewSet):
    """

    """
    model = MobUserStatus


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]





