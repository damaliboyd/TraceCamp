from django.db import models

class Animal(models.Model):
    name = models.TextField()
    animal_id = models.IntegerField();
    age = models.TextField()
    species = models.TextField()
    description = models.TextField()
    url = models.URLField()
    location = models.TextField()
    liked = models.BooleanField()


class Image(models.Model):
    img = models.URLField()
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE, relate_name='image')

class Contact(models.Model):
    email = models.EMAILField()
    phone = models. IntegerField()
    animal = models.OneToOneField(Animal, on_delete = models.CASCADE, relate_name='image')

class Address(models.Model):
    city = models.TextField()
    state = models.TextField()
    zip = models.TextField()
    country = models.TextField()
    animal = models.OneToOneField(Animal, on_delete = models.CASCADE, relate_name='addr')
