from django import forms
from mechanics.models import Mechanics
from django.contrib.auth.models import User


class RegisterMechanicForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Mechanics
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = Mechanics.objects.get(email=email)
        except Mechanics.DoesNotExist:
            return email
        raise forms.ValidationError("The Email is already Registered")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            match = Mechanics.objects.get(username=username)
        except Mechanics.DoesNotExist:
            return username
        raise forms.ValidationError("Username taken, please try another one")

class UpdateMechanicForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Mechanics
        fields = '__all__'

