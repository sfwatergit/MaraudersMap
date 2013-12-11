import datetime
from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices, FieldTracker
from model_utils.fields import StatusField, MonitorField
from MaraudersMap import settings

last_online_duration = getattr(settings, 'LAST_ONLINE_DURATION', 900)

class LocationFix(models.Model):
    """This is concrete location data updated directly from the relevant
    localization stratagems (semantic and SMT solver) via the RESTful
    interface.
    This model also inherits from TimeStampedModel (see @model_utils.models)
    to determine the update time.


    >>> a = LocationFix.objects.create(name='Cory Hall')
    >>> a.room = '204'
    >>> a.current_fix.previous('title')
    """
    STRATAGEMS = Choices('SMT', 'ML', 'User-Validated')
    #User-specific
    uuid = models.CharField(max_length=32)
    epoch = models.DateTimeField()
    #Location-specific
    country = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    building = models.CharField(max_length=32)
    floor = models.CharField(max_length=5)
    room = models.CharField(max_length=25)

    #Optional derived fields
    strategy = models.CharField(choices=STRATAGEMS, default=STRATAGEMS.ML,
                                max_length=5)
    confidence = models.IntegerField('The confidence of the '
                                     'aggregate localization measurement '
                                     'for this particular report, if '
                                     'available.', null=True, blank=True,
                                     default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.building


    class Meta:
        unique_together = (("building", "epoch", "floor", "room", "uuid"),)





class MobUserManager(models.Manager):
    def onlines(self):
        now = datetime.now()
        return MobUserStatus.objects.filter( \
            updated_on__gte=now - datetime.timedelta(seconds=last_online_duration) \
            )

    def online_users(self):
        return self.onlines().filter(user__isnull=False)



class MobUserStatus(models.Model):
    """They may be in one of many Rooms in a Building. The
    location is tied to the device_id
    """
    #TODO: Need to make sure that only owner objects are updated in serializer
    user = models.OneToOneField(User, related_name='status_of')
    STATUS = Choices('online', 'offline')
    status = StatusField()
    location_fix = models.ForeignKey(LocationFix, related_name='of_user', to_field='id')
    status_changed = MonitorField(monitor='status')
    location_changed = FieldTracker(fields=['location_fix'])

    objects = MobUserManager()

    def online(self):
        now = datetime.now()
        if (now - self.status_changed).seconds < last_online_duration:
            return True
        return False
