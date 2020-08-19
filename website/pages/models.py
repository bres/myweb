from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Landing_content(models.Model):
    body=models.TextField()
    pub_date=models.DateField()

class Post(models.Model):
    tags=models.CharField(max_length=100 ,blank=True)
    title=models.CharField(max_length=200)
    Blog_title_tag=models.CharField(max_length=200,default="The Blog Title Tag")
    image=models.ImageField(upload_to='images/',null=True, blank=True  )
    pub_date=models.DateField()
    body=models.TextField(blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
       ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('ArticleDetail', args=[self.id])

class Project(models.Model):
    title=models.CharField(max_length=200)
    Project_title_tag=models.CharField(max_length=200,default="The Project Title Tag")
    image=models.ImageField(upload_to='images/',null=True, blank=True  )
    pub_date=models.DateField()
    body=models.TextField(blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
