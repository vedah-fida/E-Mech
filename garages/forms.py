from garages.models import RegisterGarage
from django.forms import ModelForm
from django import forms

"""
class RegisterGarageF(forms.Form):
    garage_name = forms.CharField(max_length=23, label="Enter a Garage Name")
    garage_location = forms.CharField(max_length=50, label="Enter your Garage Location")
    garage_email = forms.EmailField(label="Enter Your Garage Email Address")
    garage_telephone = forms.IntegerField(label="Enter Your Garage Telephone Number")

    def clean(self, *args, **kwargs):
        garage_name = self.cleaned_data.get("garage_name")
        queryset = RegisterGarage.objects.filter(garage_name=garage_name)
        if queryset.exists:
            raise forms.ValidationError("Garage Already Exists")
        
        return super(RegisterGarageF, self).clean()
"""


class RegisterGarageForm(ModelForm):
    class Meta:
        model = RegisterGarage
        fields = '__all__'

    # check if garage name exists
    """
    def clean_garage_name(self):
        pass
    """

class EditUpdateGarageForm(ModelForm):
    class Meta:
        model = RegisterGarage
        fields = '__all__'


