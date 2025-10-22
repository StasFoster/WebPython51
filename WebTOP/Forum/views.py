from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from . import forms, models

# Create your views here.

@never_cache
def forum(request):
    threads = models.Thread.objects.all()


    data = {"is_signin": False, "threads": threads}

    if request.user.is_authenticated:
        data["is_signin"] = True

    return render(request, 'Forum/index.html', data)

@never_cache
def addThread(request):
    if not request.user.is_authenticated:
        return redirect("register")
    if request.method == "POST":
        form = forms.ThreadForm(request.POST)
        if form.is_valid():
            thread = models.Thread(title=form.cleaned_data["title"], content=form.cleaned_data["content"], author=request.user)
            thread.save()
            return redirect("forum")
    else:
        form = forms.ThreadForm()
    return render(request, "Forum/addThread.html", {"form" : form})
