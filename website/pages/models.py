from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Landing_content(models.Model):
    body=models.TextField()
    pub_date=models.DateField()

class Post(models.Model):
    tags=models.CharField(max_length=100 ,blank=True)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/',null=True, blank=True  )
    pub_date=models.DateField()
    body=models.TextField(blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)



class Project(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/',null=True, blank=True  )
    pub_date=models.DateField()
    body=models.TextField(blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
