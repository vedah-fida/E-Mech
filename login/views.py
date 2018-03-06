from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from login.forms import UserLoginForm


# Create your views here.


def login_user(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect to the services landing page
            return HttpResponseRedirect(reverse("services:services-landing"))
        else:
            return HttpResponseRedirect(reverse("login:login_user"))
    else:
        form = UserLoginForm()

    return render(request, "login/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login:login_user"))
