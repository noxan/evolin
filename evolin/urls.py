from django.conf.urls import patterns, include, url
from django.contrib import admin

from evolin.api import api_v1


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(api_v1.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
