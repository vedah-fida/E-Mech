from django.conf.urls import url, include

from garages.views import *

app_name = "garages"

# url patterns
urlpatterns = [
    url(r'^$', all_garages, name="all_garages"),
    url(r'^add/$', register_garage, name="register_garage"),
    url(r'^add/(?P<pk>[0-9]+)/$', edit_garage, name="edit_garage"),
]

