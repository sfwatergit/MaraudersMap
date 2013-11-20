from django.conf.urls import patterns, url

urlpatterns = patterns('semantic_mapping.views',
                       # geojson
                       url(r'^geojson/$', 'geojson_location_list',
                           name='api_geojson_location_list'),
                       url(r'^geojson/(?P<pk>[0-9]+)/$',
                           'geojson_location_details',
                           name='api_geojson_location_details'),
                       # Filters
                       url(r'^filters/contained_in_bbox$',
                           'geojson_location_contained_in_bbox_list',
                           name='api_geojson_building_list_contained_in_bbox_filter'),
                       url(r'^filters/overlaps_bbox$',
                           'geojson_location_overlaps_bbox_list',
                           name='api_geojson_building_list_overlaps_bbox_filter'),
)