from django.shortcuts import render
from .models import Landing_content
# Create your views here.


def home(request):
    all_items=Landing_content.objects.all

    return render(request,"home.html",{'all_items':all_items})

def about(request):
    return render(request,"about.html",{})

def projects(request):
    return render(request,"projects.html",{})

def blog(request):
    return render(request,"blog.html",{})

def contact(request):
    return render(request,"contact.html",{})