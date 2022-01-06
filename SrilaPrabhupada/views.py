from django.shortcuts import render
from .models import *


# Create your views here.
def archana(request):
    data = Archana.objects.all().values()
    context = dict()
    context['data'] = data

    return render(request, 'archana.html',context)

def biography(request):
    data = Biography.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request, 'biography.html',context)

def books(request):
    data = Books.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request, 'books.html',context)

def lectures(request):
    return render(request, 'lectures.html')

def bhajana(request):
    return render(request, 'bhajana.html')
