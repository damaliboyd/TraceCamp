from django.db import models

# Create your models here.

class Animal:
    name = models.TextField()
    age = models.IntegerField()
    image = models.URLField()
    

    