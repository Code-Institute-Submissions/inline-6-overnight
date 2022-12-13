from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    """
    Class to create form fields for the signup page
    """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AuthenticationForm(AuthenticationForm):
    """
    Class to create form fields for the login page
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "password")

    def save(self, commit=True):
        user = super(AuthenticationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.password = self.cleaned_data["password"]
        if commit:
            user.save()
        return user
