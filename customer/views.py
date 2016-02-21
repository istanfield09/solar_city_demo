from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from django.forms.models  import model_to_dict
# Create your views here.

def customerInfoView(request):

    if request.method == "GET":
        pass
    elif request.method == "POST":
        cid = request.POST['customerId']

        customer = customerData()
        fieldDict = model_to_dict(customer)

        for field in fieldDict:
            if field in request.POST:
                inputValue = request.POST[field]
                setCustomerField(customer, field, inputValue)

        customer.save()



    return HttpResponse("OK")
