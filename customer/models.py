from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.
class CustomerManager(models.Manager):
    def create_customer(self, clientPayload):
        fn = clientPayload['firstName']
        ln = clientPayload['lastName']
        sa = clientPayload['streetAddress']
        st = clientPayload['state']
        zc = clientPayload['zipcode']
        cm = clientPayload['contactMessage']

        cd = datetime.datetime.utcnow()

        customer = self.create(firstName = fn, lastName = ln, streetAddress = sa, state = st, zipcode = zc, contactMessage = cm, contactDate = cd)
        return customer

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)

    streetAddress = models.CharField(max_length=255)
    state = models.CharField(max_length=18)
    zipcode = models.PositiveIntegerField()

    contactDate = models.DateField()
    contactMessage = models.TextField()

    objects = CustomerManager()

