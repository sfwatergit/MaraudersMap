from django.test import TestCase
from semantic_mapping.models import LocationFix


class LocationFixTestCase(TestCase):
    fixtures = ['marauders_map_testdata.json']

    def setUp(self):
        super(LocationFixTestCase, self).setUp()
        self.loc_fix1 = LocationFix.objects.get(pk=1)
        self.loc_fix1 = LocationFix.objects.get(pk=2)
