from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm



class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")