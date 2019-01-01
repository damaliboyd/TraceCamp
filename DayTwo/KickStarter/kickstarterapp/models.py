from django.db import models

# Create your models here.
class Kickstarter(models.Model):
    backers_count = models.IntegerField()
    blurb = models.TextField()
    category = models.TextField()
