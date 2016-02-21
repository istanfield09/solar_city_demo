from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict

# Create your models here.

def setCustomerField(customer,fieldName, fieldValue):
    customer.setField(fieldName, fieldValue)

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

    def setField(self, fieldName, fieldValue):
        self.fieldName = fieldValue
