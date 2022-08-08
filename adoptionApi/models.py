 
from django.db import models
from rest_framework.permissions import IsAuthenticated
from phonenumber_field.modelfields import PhoneNumberField

 
# Create your models here.


class Animal(models.Model):
    permission_classes = [IsAuthenticated]

    GENDER_CHOICES=[
        ('MALE','Male'),
        ('FEMALE','Female')
    ]
    ANIMAL_CHOICES=[
        ('Cat','Cat') ,
        ('Dog','Dog'),
        ('Other','Other'),

    ]
    name = models.CharField(max_length=20)
    animal= models.CharField(max_length=10,choices=ANIMAL_CHOICES)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    breed= models.CharField(max_length=25)
    age=models.CharField(max_length=20)
    caretaker= models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    contactNumber= PhoneNumberField(region='IN') 

    def __str__(self):
        return self.name
