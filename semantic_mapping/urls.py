from django.conf.urls import patterns, url
from semantic_mapping import views

urlpatterns = patterns('semantic_mapping.views',


                       url(r'^buildings/$',
                           'building_list',
                           name='api_building-list'),

                       url(r'^buildings/(?P<name>[-\w]+)/$',
                           'building_details',
                           name='api_building-details'),

                       url(r'^buildings/(?P<name>[-\w+]+)/floors/$',
                           'floor_list',
                           name='api_floor-list'),

                       url(r'^buildings/(?P<name>[-\w]+)/floors/(?P<level>[0-9]+)/$',
                           'floor_details',
                           name='api_floor-details'),
                       url(r'^buildings/(?P<name>[-\w]+)/floors/(?P<level>[0-9]+)/rooms$',
                           'room_list',
                           name='api_room-list'),

                       url(r'^buildings/(?P<name>[-\w]+)/floors/(?P<level>[0-9]+)/rooms/(?P<room_number>[0-9]+)/',
                           'room_details',
                           name='api_room-details'),
                       )


