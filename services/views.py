from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login:login_user')
def servicesLanding(request):
    page_name = "Services Dashboard"
    user = User.is_authenticated
    return render(request, 'services/landing.html', {"page_name": page_name, "user": user})


@login_required(login_url='login:login_user')
def carRepair(request):
    page_name = "Car Repair"
    i = 0
    context = {
        "page_name": page_name,
        "i": i
    }

    return render(request, 'services/carRepair.html', {"context": context})


@login_required(login_url='login:login_user')
def towTruck(request):
    name = "Tow truck service coming soon"
    return HttpResponse(name)


@login_required(login_url='login:login_user')
def medicalHelp(request):
    name = "Medical Help service coming soon"
    return HttpResponse(name)
