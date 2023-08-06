from django.db import models

# Create your models here.
class superadmins(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=20)

class vehiclemodel(models.Model):
    choice = [
        ('two','two'),
        ('three','three'),
        ('four','four')
    ]
    Vehiclenumber=models.CharField(max_length=10)
    Vehicletype=models.CharField(max_length=30,choices=choice)
    vehiclemodel=models.CharField(max_length=30)
    vehicledesc=models.CharField(max_length=90)
    def __str__(self):
        return self.vehiclemodel

class admins(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

