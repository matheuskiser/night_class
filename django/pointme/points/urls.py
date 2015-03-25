from django.conf.urls import patterns, url

from points import views

urlpatterns = patterns('',
    url(r'^$', views.show_places, name='index'),
)