from rest_framework import serializers
from django.contrib.auth.models import User


class MobUserSerializer():
"""
{
  "device": {
    "uuid": "1d352410-4a5e-11e3-8f96-0800200c9a66"
  },
  "epoch": 1384125523375
}
"""


class LocalizationSerializer():
"""
{
  "semloc": {
    "country": "US",
    "state": "CA",
    "city": "Berkeley",
    "street": "Leroy Ave",
    "building": "Soda Hall",
    "floor": "Floor 4",
    "room": "494"
  },
"""
