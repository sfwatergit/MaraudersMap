from rest_framework.routers import DefaultRouter
from marmap_users.views import LocationViewSet, MobUserStatusViewSet, UserViewSet


router = DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'status', MobUserStatusViewSet)
router.register(r'users', UserViewSet)
urlpatterns = router.urls

#urlpatterns += patterns('marmap_users.views',)
