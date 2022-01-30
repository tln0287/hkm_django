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
    data = Lectures.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request, 'lectures.html',context)

def bhajana(request):
    data = Bhajans.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request, 'bhajana.html',context)

def bbooks(request):

    return render(request, 'bbooks.html')
