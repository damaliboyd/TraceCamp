from django.db import models

# Create your models here.

class Image:
    url = models.URLField()

class Animal:
    name = models.CharField()
    age = models.IntegerField()
    breed = models.CharField()
    images = models.ForeignKey('Image', on_delete = models.CASCADE)
    description = models.TextField()
    location = models.IntegerField()
    


    