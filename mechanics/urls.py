from django.conf.urls import url
from mechanics.views import all_mechanics

app_name = "mechanics"

urlpatterns = [
    url('^$', all_mechanics, name="all_mechanics"),

]
