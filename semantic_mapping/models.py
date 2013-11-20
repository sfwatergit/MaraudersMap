# coding=utf-8
"""
Note that the only dynamic (i.e., regularly updating) fields are located on
the location_fix and mob_user.
"""
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField
from django_states.machine import StateMachine
from model_utils import Choices, FieldTracker

from django.contrib.gis.db import models
from model_utils.fields import StatusField, MonitorField
from model_utils.models import TimeStampedModel, StatusModel
from datetime import datetime
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class LocationFix(TimeStampedModel):
    """This is concrete location data updated directly from the relevant
    localization stratagems (semantic and SMT solver) via the RESTful
    interface.
    This model also inherits from TimeStampedModel (see @model_utils.models)
    to determine the update time.


    >>> a = LocationFix.objects.create(name='Cory Hall')
    >>> a.room = '204'
    >>> a.current_fix.previous('title')
    """

    uuid = UUIDField(max_length=32)
    epoch = models.DateTimeField()
    country = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    building = models.CharField(max_length=25)
    floor = models.CharField(max_length=4)
    room = models.CharField(max_length=25)
    current_fix = FieldTracker(fields=['room'])

    def __unicode__(self):
        """

        :rtype : object
        """
        return "%s" % self.uuid

    def save(self, *args, **kwargs):
        if isinstance(self.epoch, datetime.__class__):
            return self.epoch
        else:
            return datetime.utcfromtimestamp(self.epoch)


class LocationFixSource(models.Model):
    STRATAGEMS = Choices('SMT', 'ML')
    strategy = models.CharField(choices=STRATAGEMS, default=STRATAGEMS.ML,
                                max_length=5)
    confidence = models.IntegerField('The confidence of the '
                                     'aggregate localization measurement '
                                     'for this particular report, if '
                                     'available.', null=True, blank=True)


class Building(models.Model):
    """Buildings have several Floors. The building may have a specific
    address. We won't be assigning spatial data here, but we will aggregate info
     on buildings.

    """
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"))

    longitude = models.FloatField(_("Longitude"), blank=True, editable=False)
    latitude = models.FloatField(_("Latitude"), blank=True, editable=False)
    position = models.PointField(_("Position"), srid=4326, blank=True,
                                 null=True)
    street = models.CharField(_("Street"), blank=True, max_length=250)
    postal_code = models.CharField(_("Postal code"), blank=True,
                                   max_length=25)
    city = models.CharField(_("City"), blank=True, max_length=100)

    description = models.TextField(_("Description"), blank=True)

    added_on = models.DateTimeField(default=datetime.now, editable=False)
    updated_on = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    @models.permalink
    def get_absolute_url(self):
            return ('places-detail', [self.slug])

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Updating latitude/longitude when position is updated
        """
        if self.position:
            self.latitude = self.position.x
            self.longitude = self.position.y
        self.updated_on = datetime.now()
        super(Building, self).save(*args, **kwargs)


class Floor(models.Model):
    """Each Floor in a Building is a MultiPolygon of Rooms.
    There will be an image associated with this model representing
    the map."""
    building = models.ForeignKey(Building)
    level = models.IntegerField(max_length=5)
    assoc_map = models.ImageField(upload_to='/data')
    poly = models.MultiPolygonField()
    objects = models.GeoManager()


class Room(models.Model):
    """A room may have many MobUsers and vice-versa.
    We will be representing each Room with a polygon."""
    floor = models.ForeignKey(Floor)
    room_number = models.IntegerField()
    poly = models.PolygonField()
    objects = models.GeoManager()


class MobUserProfile(models.Model):
    """These are the participants visualized on the Map.
    They may be in one of many Rooms in a Building. The
    location is tied to the device_id and the epoch.

    """
    mob_user = models.OneToOneField(User)
    device_id = models.CharField(max_length=32)


class MobUserState(models.Model):
    """Implement the mobile_phone user's state as a state machine.
    Many of these are implemented on the field tracker for convenience.


    """
    log_transitions = True


    mob_user = models.ForeignKey(MobUserProfile)


from south.modelsinspector import add_introspection_rules

add_introspection_rules([],
    ["^django\.contrib\.gis\.db\.models\.fields\.PointField"])







