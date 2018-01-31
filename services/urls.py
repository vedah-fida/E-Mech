from django.conf.urls import url
from .views import *

app_name = "services"

urlpatterns = [

    url(r'^$', servicesLanding, name="services-landing"),

    url(r'^car-repair/', carRepair, name="car-repair"),

    url(r'^tow-truck/', towTruck, name="tow-truck"),

    url(r'^medical-help/', medicalHelp, name="medical-help"),
]