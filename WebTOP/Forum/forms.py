from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ThreadForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


