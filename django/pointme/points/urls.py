from django.conf.urls import patterns, url

from points import views

urlpatterns = patterns('',
    url(r'^$', views.show_places, name='index'),
    url(r'^add_place/$', views.add_place, name='add_place'),
    url(r'^my_places/$', views.my_places, name='my_places'),
    url(r'^map_view/$', views.map_view, name='map_view'),
)