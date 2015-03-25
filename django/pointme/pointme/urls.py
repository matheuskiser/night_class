from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^points/', include('points.urls', namespace="points")),
    url(r'^admin/', include(admin.site.urls)),
)
