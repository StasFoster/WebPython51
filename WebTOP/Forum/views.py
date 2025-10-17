from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout

# Create your views here.
@never_cache
def forum(request):
    data = {"is_signin": False}

    if request.user.is_authenticated:
        data["is_signin"] = True

    return render(request, 'Forum/index.html', data)



