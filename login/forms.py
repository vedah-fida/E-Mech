from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # if username and password:
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("The User does not exist")

        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")

        """if not user.is_active():
            raise forms.ValidationError("The user is no longer active")
        """

        return super(UserLoginForm, self).clean()
