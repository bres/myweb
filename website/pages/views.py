from django.shortcuts import render
from .models import Landing_content,Posts
# Create your views here.


def home(request):
    all_items=Landing_content.objects.all
    all_posts = Posts.objects.all
    return render(request,"home.html",{'all_items':all_items,'all_posts':all_posts})

def about(request):
    return render(request,"about.html",{})

def projects(request):
    return render(request,"projects.html",{})

def blog(request):
    all_posts=Posts.objects.all
    return render(request,"blog.html",{'all_posts':all_posts})

def contact(request):
    return render(request,"contact.html",{})