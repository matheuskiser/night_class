from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    author = models.ForeignKey(User)
    address = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    like = models.BooleanField(default=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    comment = models.CharField(max_length=10000)

    def __str__(self):
        return self.name