from django.conf.urls import url
from .views import *

app_name = "garages-api"
urlpatterns = [
    url(r'^all-garages/$', GaragesListCreate.as_view(), name="garages-list-create-view"),
    url(r'^all-garages/(?P<pk>[0-9]+)/$', GaragesRetrieve.as_view(), name="garages-list-view"),

]
