from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Animal(models.Model):
    GENDER_CHOICES=[
        ('MALE','Male'),
        ('FEMALE','Female')
    ]
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    breed= models.CharField(max_length=25)
    age=models.CharField(max_length=20)
    caretaker= models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    contactNumber= PhoneNumberField(region='IN')

    def __str__(self):
        return self.name
