"""EMech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('login.urls')),
    url(r'^mechanics/', include('mechanics.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^garages/', include('garages.urls')),

    url(r'^mechanics-api/', include('mechanics.api.urls'), name="mechanics-api"),
    url(r'^garages-api/', include('garages.api.urls'), name="garages-api"),
]
