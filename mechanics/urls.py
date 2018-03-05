from django.conf.urls import url, include

from mechanics.views import *

app_name = "mechanics"

# url patterns
urlpatterns = [

    #api urls

    #non-api urls
    url(r'^$', all_mechanics, name="all_mechanics"),

    #connect to the api
    #url(r'^api', include('api.urls')),
]
