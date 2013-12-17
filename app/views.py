from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from django.views.generic import TemplateView
from djgeojson.serializers import Serializer as GeoJSONSerializer
from requests import Response

from semantic_mapping.models import *

@csrf_exempt
class MapView(TemplateView):
    template_name = 'map.html'

@ensure_csrf_cookie
def floor_layer(request, *args, **kwargs):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    geojson = GeoJSONSerializer().serialize(
        Building.objects.filter(name=kwargs['building'])[0].floors.filter(level=kwargs['floor'])[
            0].rooms.all())
    response.write(geojson)
    return response

