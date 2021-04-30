from django.db import models
from datetime import date, datetime


class Movies(models.Model):

    name = models.CharField(max_length=250,  default='NA')
    director = models.CharField(max_length=1000, default='NA')
    genere = models.CharField(max_length=1000, default='NA')
    rating = models.IntegerField(default=0)
    release_date = models.DateTimeField(default=date.today)


# id name director genere rating release date

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
