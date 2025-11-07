# from django.http import HttpResponse
from importlib.resources import contents

from django.shortcuts import render, redirect
from django.template.defaulttags import comment
from django.views.decorators.cache import never_cache
# from django.contrib.auth import logout
from . import forms,models
from .models import Product


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
        return redirect('register')
    if request.method == "POST":
        form = forms.ThreadForm(request.POST)
        if form.is_valid():
            thread = models.Thread(title=form.cleaned_data['title'], content=form.cleaned_data['content'], author=request.user)
            thread.save()
            return redirect('forum')
    else:
        form = forms.ThreadForm()
    return render(request, 'Forum/AddThread.html', {"form": form})

def pageThreads(request,id):
    thread = models.Thread.objects.get(id=id)
    comments = thread.comments.all()


    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.MyComment(content=form.cleaned_data['comment'], author=request.user,thread=thread)
            comment.save()
            thread.comments.add(comment)
        return render(request, 'Forum/page.html', { "is_signin": request.user.is_authenticated,"thread": thread, "comments": comments,"form": form})
    else:
        form = forms.CommentForm()





    return render(request,"Forum/page.html", {"is_signin": request.user.is_authenticated,"thread":thread, "comments":comments,"form": form})



def products_list(request):
    
    products = Product.objects.all()[:3]
    
    
    return render(request, 'Forum/Store', {'Product': products
      
    })



