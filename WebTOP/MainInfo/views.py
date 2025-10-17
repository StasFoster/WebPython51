from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def index(request):
    if request.method == "POST":
        form = forms.MainInfoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("forum")

    else:
        form = forms.MainInfoForm()
    data  = {

        'form': form,
    }
    return render(request, 'MainInfo/index.html', data)


def out(request):
    logout(request)
    return redirect("forum")

def sign_in(request):
    if request.method == "POST":
        form = forms.LoginForm(data=request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request,user)
                return redirect("forum")
            else:
                return redirect("register")

    else:
        form = forms.LoginForm()
    return render(request,"MainInfo/index.html",{'form': form})


