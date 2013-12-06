from django.conf.urls import patterns, url
from semantic_mapping import views

urlpatterns = patterns('semantic_mapping.views',


                       url(r'^buildings/$',
                           'building_list',
                           name='api_building-list'),

                       url(r'^buildings/(?P<name>[-\w]+)/$',
                           'building_details',
                           name='api_building-details'),

                       url(r'^buildings/(?P<building>[-\w+]+)/floors/$',
                           'floor_list',
                           name='api_buildingfloor-list'),

                       url(r'^buildings/(?P<building>[-\w]+)/floors/(?P<level>[\d+]+)/$',
                           'floor_details',
                           name='api_floor-details'),
                       url(r'^buildings/(?P<building>[-\w]+)/floors/(?P<level>[\w+]+)/rooms$',
                           'floorroom_list',
                           name='api_floorroom-list'),

                       url(r'^buildings/(?P<name>[-\w]+)/floors/(?P<level>[\w+]+)/rooms/(?P<room>[\w+]+)/',
                           'room_details',
                           name='api_room-details'),
                       )


