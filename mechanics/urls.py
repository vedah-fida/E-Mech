from django.conf.urls import url, include

from mechanics.views import all_mechanics, register_mechanic, mechanic_details

app_name = "mechanics"

# url patterns
urlpatterns = [
    url(r'^$', all_mechanics, name="all_mechanics"),
    url(r'^add/$', register_mechanic, name="register_mechanic"),
    url(r'^add/(?P<pk>[0-9]+)/$', mechanic_details, name="mechanic_details"),
]
