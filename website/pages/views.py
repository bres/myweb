from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import PostForm
######################################################################
# nav views
def home_nav(request):
    all_items=Landing_content.objects.all
    latest_post = Post.objects.last()
    return render(request,"home.html",{'all_items':all_items,'latest_post':latest_post})

def about_nav(request):
    return render(request,"about.html",{})

def projects_nav(request):
    all_projects=Project.objects.all
    return render(request,"projects.html",{'all_projects':all_projects})

def blog_nav(request):
    all_posts=Post.objects.order_by('-id')
    return render(request,"blog.html",{'all_posts':all_posts})

def contact_nav(request):
    return render(request,"contact.html",{})

######################################################################
# dashboard views
def createPost(request):
        form = PostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            form = PostForm()
            return redirect('createPost')
        context=Post.objects.all
        return render(request,"dashboard.html",{'form':form,'context':context})

def dashboard(request):
    context=Post.objects.all
    return render(request,"dashboard.html",{'context':context})
