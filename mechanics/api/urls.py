from django.conf.urls import url, include
from django.contrib import admin
from .views import MechanicCRUDView

urlpatterns = [
    url(r'^(?P<id>d+)/', MechanicCRUDView.as_view(), name="mechanic-crud"),
]
