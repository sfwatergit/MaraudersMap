from django.conf.urls import *
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from semantic_mapping.models import Room, Floor

urlpatterns = patterns('app.views',
                       url('^map/$', TemplateView.as_view(template_name='map.html'), name='map'),
                       url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Room), name='rooms'),
                       url(r'^floor.geojson$', GeoJSONLayerView.as_view(model=Floor), name='floors'),
                       url(r'^(?P<building>[-\w]+)/(?P<floor>[-\d]+)/data.geojson', 'floor_layer',
                           name='both'),

                       )
