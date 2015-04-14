from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    author = models.ForeignKey(User)
    address = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name