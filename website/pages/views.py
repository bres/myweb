from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import PostForm
from django.views.generic import ListView,DetailView
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

class blog(ListView):
    model=Post
    template_name='blog.html'

class ArticleDetail(DetailView):
    model=Post
    template_name='article_details.html'


def contact(request):
    return render(request,"contact.html",{})
