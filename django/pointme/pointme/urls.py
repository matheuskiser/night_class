from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/points/'

urlpatterns = patterns('',
    url(r'^points/', include('points.urls', namespace="points")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
