from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth import login, logout;
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



