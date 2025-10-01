from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth import login

# Create your views here.
def index(request):
    # if request.method == "POST":
    #     form = forms.MainInfoForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect("index")
    #
    # else:
    #     form = forms.MainInfoForm()
    form = forms.EventForm()
    data  = {
        'form': form,
    }
    return render(request, 'MainInfo/index.html', data)


def home(request):
    users = models.MyUser.objects.all()
    data = {}
    if users:
        data = {
            'list_users': [i.username for i in users],
        }
    return render(request, 'MainInfo/home.html', data)