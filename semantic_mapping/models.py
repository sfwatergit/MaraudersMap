# coding=utf-8
"""
Note that the only dynamic (i.e., regularly updating) fields are located on
the location_fix and mob_user.
"""

from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Building(models.Model):
    """Buildings have several Floors. The building may have a specific
    address.

    """
    name = models.CharField(max_length=200)
    street = models.CharField(blank=True, max_length=250)
    postal_code = models.CharField(blank=True,
                                   max_length=25)
    city = models.CharField(blank=True, max_length=100)
    geom = models.PointField(dim=2, srid=4326, blank=True,
                                 null=True)

    objects = models.GeoManager()

    def getGeometry(self):
        return self.geom

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')




class Floor(models.Model):
    """Each Floor in a Building is a Polygon of Rooms.
    There will be an image associated with this model representing
    the map."""
    building = models.ForeignKey(Building, related_name='floors')
    level = models.IntegerField(max_length=5)
    geom = models.PolygonField(dim=2, srid=4326, null=True, blank=True)
    objects = models.GeoManager()

    def getGeometry(self):
        return self.geom


class Room(models.Model):
    """A room may have many MobUsers.
    We will be representing each Room with a polygon."""
    floor = models.ForeignKey(Floor, related_name='rooms')
    room = models.CharField(max_length=100, null=True)
    geom = models.PolygonField(dim=2, srid=4326, null=True, blank=True)

    objects = models.GeoManager()


from south.modelsinspector import add_introspection_rules
add_introspection_rules([],
    ["^django\.contrib\.gis\.db\.models\.fields\.PointField"])







