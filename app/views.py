from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView, GeoJSONResponseMixin
from semantic_mapping.models import *


class MapView(TemplateView):
    template_name = 'map.html'


class FloorLayer(GeoJSONResponseMixin, TemplateView):
    model = Floor

    def get_queryset(self, *args, **kwargs):
        return Building.objects.filter(name=self.kwargs['building'])[0].floors.filter(level=self.kwargs['floor'])[0]\
            .rooms.all()

floor_layer = FloorLayer.as_view()

class RoomLayer(GeoJSONResponseMixin, TemplateView):
    model = Room

    def get_queryset(self, *args, **kwargs):
        b_id = Building.objects.filter(name=self.kwargs['building'])[0].id
        f_id = Floor.objects.filter(level=self.kwargs['floor'])[0].id


room_layer = RoomLayer.as_view()