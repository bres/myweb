
from django.contrib import admin
from django.urls import path
from .import views
from .views import blog,ArticleDetail,AddPostView

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('blog/',blog.as_view(),name='blog'),
    path('article/<int:pk>',ArticleDetail.as_view(),name='ArticleDetail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),

    path('contact/',views.contact,name='contact'),


]
