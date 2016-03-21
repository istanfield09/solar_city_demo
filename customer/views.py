from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

import datetime

from models import Customer

import json
# Create your views here.

def customerInfoView(request):

    if request.method == "GET":
        pass

    elif request.method == "POST":
        customerData = json.loads(request.body)['customer']
        print customerData

        customer = Customer.objects.create_customer(customerData)
        customer.save()

        print customerData

    context = {"stuff": "more stuff"}

    return render(request, "index.html", context)
