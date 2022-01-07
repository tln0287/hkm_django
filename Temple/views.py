from django.shortcuts import render
from .models import *
# Create your views here.

def templehistory(request):
    data = TempleHistory.objects.all().values()
    context = dict()
    context['data'] = data

    return render(request,'templehistory.html', context)

def facilities(request):
    data = Facilities.objects.all().values()
    context = dict()
    context['data'] = data

    return render(request,'facilities.html', context)

def guesthouse(request):
    data = GuestHouse.objects.all().values()
    context = dict()
    context['data'] = data

    return render(request,'guesthouse.html', context)