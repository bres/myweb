from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import PostForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    all_items=Landing_content.objects.all
    latest_post = Post.objects.first()
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

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    #fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='update_post.html'
    #fields='__all__'

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    #fields='__all__'
    success_url =reverse_lazy('blog')

def contact(request):
    return render(request,"contact.html",{})
