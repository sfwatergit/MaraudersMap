from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from marmap_users.views import LocationViewSet, MobUserStatusViewSet, UserViewSet, OnlineUserView, onlineusers


router = DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'status', MobUserStatusViewSet)
router.register(r'all-user', UserViewSet)


urlpatterns = router.urls


urlpatterns += patterns('marmap_users.views',
                        url(r'^online-users/(?P<building>[-\w]+)/(?P<floor>[-\w]+)', onlineusers))
