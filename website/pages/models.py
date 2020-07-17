from django.db import models

# Create your models here.
class Landing_content(models.Model):
    body=models.TextField()
    pub_date=models.DateField()

class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateField()
    image=models.ImageField(upload_to='images/',blank=True)
    tags=models.CharField(max_length=100 ,blank=True)

class Project(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/',blank=True)
    pub_date=models.DateField()
    body=models.TextField(blank=True)
 
    def __str__(self):
        return self.body + self.title
