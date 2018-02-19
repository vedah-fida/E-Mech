from django.conf.urls import url
from .views import *
app_name = "api"
urlpatterns = [
    url(r'', test_view, name="test_view"),

]
