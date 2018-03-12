from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterMechanicForm, UpdateMechanicForm
from .models import Mechanics
from django import forms


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

"""
def mechanic_details(request, pk):

    #form = UpdateMechanicForm()
    try:
        mechanic = Mechanics.objects.get(pk=pk)
        form = UpdateMechanicForm(request.POST, instance=mechanic)

    except Mechanics.DoesNotExist:
        return HttpResponse("Object not found")
    return render(request, 'mechanics/get_mechanic.html', {'mechanic': mechanic, 'form': form})
"""

def mechanic_details(request, pk):
    mechanic_instance = get_object_or_404(Mechanics, pk=pk)
    form = UpdateMechanicForm(request.POST or None, instance=mechanic_instance)
    if form.is_valid():
       instance = form.save(commit=False)
       instance.save()
       return redirect("mechanics:register_mechanic")

    context = {
        "form" : form,
        "mechanic_instance" : mechanic_instance,
    }
    return render(request, 'mechanics/register_mechanic.html', context)