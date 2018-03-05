from django.conf.urls import url
from .views import *
app_name = "api"
urlpatterns = [
   # url(r'', MechanicListAPIView.as_view(), name="mechanic-list-api-view"),

    url(r'^all-mechanics/$', MechanicsList.as_view(), name="mechanics-list-create-view"),
    url(r'^all-mechanics/(?P<pk>[0-9]+)/$', MechanicsDetail.as_view(), name="mechanics-list-view"),

]

