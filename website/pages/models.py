from django.db import models

# Create your models here.
class Landing_content(models.Model):
    body=models.TextField()
    pub_date=models.DateField()



class Posts(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateField()
    image=models.ImageField(upload_to='images/',blank=True)



    def __str__(self):
        return self.body + self.title
