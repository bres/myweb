from django.shortcuts import render
from .models import Landing_content,Post,Project
# Create your views here.


def home(request):
    all_items=Landing_content.objects.all
    latest_post = Post.objects.last()
    return render(request,"home.html",{'all_items':all_items,'latest_post':latest_post})

def about(request):
    return render(request,"about.html",{})

def projects(request):
    all_projects=Project.objects.all
    return render(request,"projects.html",{'all_projects':all_projects})

def blog(request):
    all_posts=Post.objects.order_by('-id')
    return render(request,"blog.html",{'all_posts':all_posts})

def contact(request):
    return render(request,"contact.html",{})