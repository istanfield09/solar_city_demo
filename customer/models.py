from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CustomerData(models.Model):
    customerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    birthdate = models.DateField()

    streetAddress = models.CharField(max_length=255)
    state = models.CharField(max_length=18)
    zipcode = models.PositiveIntegerField()

    contactDate = models.DateField()
    contactMessage = models.TextField()

    operatingSystem = models.CharField(max_length=255)




