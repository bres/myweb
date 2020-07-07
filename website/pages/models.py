from django.db import models

# Create your models here.
class Landing_content(models.Model):
    body=models.TextField()
    pub_date=models.DateField()


    def __str__(self):
        return self.body
