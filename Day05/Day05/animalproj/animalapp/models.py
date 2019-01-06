from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class Animal(models.Model):
    name = models.TextField()
    age = models.TextField()
    type_of = models.TextField()
    description = models.TextField()
    location = models.IntegerField()
    liked = models.BooleanField()

    def get_absolute_url(self):
        return reverse_lazy('animal_create')

class Image(models.Model):
    url = models.URLField()
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE, related_name='image')
