from ast import Mod
from pickle import TRUE
from django.db import models

# Create your models here.
class Blog(models.Model):
    slno=models.AutoField(primary_key=TRUE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Regform(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def __str__(self): 
        return self.first_name  
