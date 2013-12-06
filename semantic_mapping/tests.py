try:
    import simplejson as json
except Exception:
    import json


from django.test import TestCase
from django.contrib.gis.geos import GEOSGeometry, Polygon
from django.core.urlresolvers import reverse

from semantic_mapping.models import *


class GeoTestCase(TestCase):

    def setUp(self):
        self.building_list_url = reverse('api_building-list')
        self.geos_error_message = 'Invalid format: string or unicode input unrecognized as WKT EWKT, and HEXEWKB.'

    def test_get_building_list(self):
        response = self.client.get(self.building_list_url)
        self.assertEqual(response.status_code, 200)

