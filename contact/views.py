from django.shortcuts import render
from .models import *

# Create your views here.


def contact(request):
    data = Contact.objects.all().values()
    media = SocialMedia.objects.all().values()
    address = data[0]['address']
    email = data[0]['email']
    phone = data[0]['phone']
    context = dict()
    context['address'] = address
    context['email'] = email
    context['phone'] = phone
    context['media'] = media
    return render(request,'contact.html',context)

def contactquery(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        obj = ContactQueries(name=name,email=email,subject=subject,message=message)
        obj.save()
        data = Contact.objects.all().values()
        media = SocialMedia.objects.all().values()
        address = data[0]['address']
        email = data[0]['email']
        phone = data[0]['phone']
        context = dict()
        context['address'] = address
        context['email'] = email
        context['phone'] = phone
        context['media'] = media
        return render(request, 'contact.html', context)
        
        