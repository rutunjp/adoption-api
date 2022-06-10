from pyexpat import model
from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
