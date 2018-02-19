from django.conf.urls import url, include

from mechanics.views import *

app_name = "mechanics"

# url patterns
urlpatterns = [
    #api urls
    url(r'^all-mechanics-view/', MechanicsView.as_view(), name="api-test"),
    url(r'^mechanics-listing-view/', MechanicsListingView.as_view(), name="mechanics-listing-view"),
    url(r'^mechanics-update-view/', MechanicUpdateView.as_view(), name="mechanics-update-view"),

    #non-api urls
    url(r'^$', all_mechanics, name="all_mechanics"),

    #connect to the api
    #url(r'^api', include('api.urls')),
]
