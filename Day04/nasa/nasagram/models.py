from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class nasagram(models.Model):
    comment = models.TextField()
    rating = models.TextField()
    favorite = models.BooleanField()
    url = models.URLField()
    date = models.DateField()

    def get_absolute_url(self):
        return reverse_lazy('detail', args = [str(self.id)])
