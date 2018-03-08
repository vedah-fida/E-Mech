from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterMechanicForm
from .models import Mechanics


# Create your views here.

@login_required(login_url='login:login_user')
def all_mechanics(request):
    all_mechanics = "<h3>The listing for all the mechanics</h3>"
    return HttpResponse(all_mechanics)


def register_mechanic(request):
    if request.method == 'POST':
        form = RegisterMechanicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Mechanic Registered Successfully")
    else:
        form = RegisterMechanicForm()

    return render(request, 'mechanics/register_mechanic.html', {'form': form})
