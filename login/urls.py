from django.conf.urls import url
from .views import *

app_name = "login"

urlpatterns = [
    url(r'^login', login_user, name="login_user"),
    url(r'^logout', logout_user, name="logout_user"),
]