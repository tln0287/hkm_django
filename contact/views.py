from django.shortcuts import render
from .models import *

# Create your views here.


def contact(request):
    data = Contact.objects.all().values()
    address = data[0]['address']
    email = data[0]['email']
    phone = data[0]['phone']
    context = dict()
    context['address'] = address
    context['email'] = email
    context['phone'] = phone
    return render(request,'contact.html',context)
