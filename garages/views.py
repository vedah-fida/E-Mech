from django.shortcuts import render
from django.http import HttpResponse
from garages.forms import RegisterGarageForm, EditUpdateGarageForm
from .models import RegisterGarage
# Create your views here.
from django import forms

def register_garage(request):
    """
    task_name = "<h3>create a new garage</h3>"
    return HttpResponse(task_name)
    """
    if request.method == 'POST':
        form = RegisterGarageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Garage Created Successfully")

    else:
        form = RegisterGarageForm()
    return render(request, 'garages/register_garage.html', {'form': form})





def edit_garage(request, pk):
    task_name = "<h3>edit an existing garage</h3>"
    return HttpResponse(task_name)



