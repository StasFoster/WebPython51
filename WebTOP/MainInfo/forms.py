from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm

class EventForm(forms.Form):
    data = forms.CharField()
    description = forms.CharField()

class MainInfoForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2']