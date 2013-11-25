from django.conf.urls import patterns, include, url

from django.contrib import admin
from MaraudersMap import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MaraudersMap.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
                       url(r'$^', include('snippets.urls')),
                       url(r'^semloc/', include('semantic_mapping.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^users/', include('marmap_users.urls')),



)
if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )