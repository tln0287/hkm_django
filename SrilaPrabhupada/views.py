from django.shortcuts import render
from .models import *

# Create your views here.
def archana(request):
    data = SrilaPrabhupada.objects.all().values()
    print(data)
    context = dict()
    context['data'] =data

    return render(request, 'archana.html',context)

def biography(request):
    return render(request, 'biography.html')

def books(request):
    return render(request, 'books.html')

def lectures(request):
    return render(request, 'lectures.html')

def bhajana(request):
    return render(request, 'bhajana.html')
