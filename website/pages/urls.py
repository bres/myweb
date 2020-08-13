
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_nav,name='home_nav'),
    path('about/',views.about_nav,name='about_nav'),
    path('projects/',views.projects_nav,name='projects_nav'),
    path('blog/',views.blog_nav,name='blog_nav'),
    path('contact/',views.contact_nav,name='contact_nav'),
    #path('dashboard/',views.dashboard,name='dashboard'),
    path('create/',views.createPost,name='createPost'),


]
