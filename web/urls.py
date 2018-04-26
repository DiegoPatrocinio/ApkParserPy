from django.conf.urls import include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from backoffice import views
from api import api


router = routers.DefaultRouter()
router.register(prefix=r'applications', viewset=api.ApplicationsAPI, base_name='applications')

admin.autodiscover()

admin.site.site_header = 'APKPARSE Admin'

urlpatterns = [
    # Examples:
    url(r'^', include('backoffice.urls')),
    url(r'^api/', include(router.urls)),

    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/', include('allauth.urls')),
]

handler404 = 'views.handle_page_not_found_404'

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
]
