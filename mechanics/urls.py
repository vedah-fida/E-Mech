from django.conf.urls import url, include

from mechanics.views import *

app_name = "mechanics"

# url patterns
urlpatterns = [
    url(r'^$', all_mechanics, name="all_mechanics"),
]
