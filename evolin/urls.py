from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from evolin.api import api_v1


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='evolin/index.html'), name='index'),
    url(r'^api/', include(api_v1.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
