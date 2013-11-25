# coding=utf-8
"""
Note that the only dynamic (i.e., regularly updating) fields are located on
the location_fix and mob_user.
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.utils.text import slugify
from django_states.models import StateModel
from model_utils import Choices, FieldTracker
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import StatusField, MonitorField
from MaraudersMap.settings import MEDIA_URL



class Building(models.Model):
    """Buildings have several Floors. The building may have a specific
    address. We won't be assigning spatial data here, but we will aggregate info
     on buildings.

    """
    name = models.CharField(_("Name"), max_length=200)
    street = models.CharField(_("Street"), blank=True, max_length=250)
    postal_code = models.CharField(_("Postal code"), blank=True,
                                   max_length=25)
    city = models.CharField(_("City"), blank=True, max_length=100)

    position = models.PointField(_("Position"), srid=4326, blank=True,
                                 null=True)


    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('semantic_mapping.views.api_building_list', args=[slugify[self.name]])


class Floor(models.Model):
    """Each Floor in a Building is a Polygon of Rooms.
    There will be an image associated with this model representing
    the map."""
    building = models.ForeignKey(Building, related_name='floors')
    level = models.IntegerField(max_length=5)
    poly = models.PolygonField(srid=4326, null=True, blank=True)
    objects = models.GeoManager()

    def getGeometry(self):
        return self.poly


class Room(models.Model):
    """A room may have many MobUsers.
    We will be representing each Room with a polygon."""
    floor = models.ForeignKey(Floor, related_name='rooms')
    room_number = models.CharField(max_length=100, null=True)
    poly = models.PolygonField(srid=4326, null=True, blank=True)

    objects = models.GeoManager()

    def getGeometry(self):
        return self.poly


from south.modelsinspector import add_introspection_rules

add_introspection_rules([],
    ["^django\.contrib\.gis\.db\.models\.fields\.PointField"])







