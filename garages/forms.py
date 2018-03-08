from garages.models import RegisterGarage
from django.forms import ModelForm
from django import forms

class RegisterGarageForm(ModelForm):
    class Meta:
        model = RegisterGarage
        fields = '__all__'

    # check if garage name exists

    def clean_garage_name(self):
        garage_name = self.cleaned_data.get('garage_name')
        try:
            registered_garage_name = RegisterGarage.objects.get(garage_name=garage_name)
        except RegisterGarage.DoesNotExist:
            return garage_name
        raise forms.ValidationError("This Garage is already Registered!")

class EditUpdateGarageForm(ModelForm):
    class Meta:
        model = RegisterGarage
        fields = '__all__'


