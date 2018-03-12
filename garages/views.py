from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from garages.forms import RegisterGarageForm, EditUpdateGarageForm
from .models import RegisterGarage
# Create your views here.
from django import forms


def register_garage(request):
    if request.method == 'POST':
        form = RegisterGarageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("garages:register_garage"))

    else:
        form = RegisterGarageForm()
    return render(request, 'garages/register_garage.html', {'form': form})


def edit_garage(request, pk):
    garage_instance = get_object_or_404(RegisterGarage, pk=pk)
    form = RegisterGarageForm(request.POST or None, instance=garage_instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(garage_instance.get_absolute_url())
    context = {
        "garage_instance": garage_instance,
        "form": form,
    }

    return render(request, 'garages/register_garage.html', context)
