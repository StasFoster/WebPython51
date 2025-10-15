from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class EventForm(forms.Form):
    data = forms.CharField(max_length=5, widget=forms.TextInput(attrs={"class":"form_group"}))
    description = forms.CharField(min_length= 4, max_length=10,widget=forms.TextInput(attrs={"class":"form_group"}))
    error_css_class = "error_field"

class MainInfoForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

