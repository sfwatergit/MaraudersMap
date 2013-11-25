from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from marmap_users.views import BuildingUserViewSet, MobUserStatusViewSet, FloorUserViewSet
from semantic_mapping import views


router = DefaultRouter()
router.register(r'buildings', BuildingUserViewSet)
router.register(r'floors', FloorUserViewSet)
router.register(r'/', MobUserStatusViewSet)
urlpatterns = router.urls

urlpatterns += patterns('marmap_users.views',
                        url(r'^(?P<building>[-\w]+)/(?P<level>[\w]+)/$',
                            'locationfix'))
