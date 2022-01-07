from django.shortcuts import render
from .models import *

# Create your views here.
def vastrabarana(request):
    data = VastrabaranaSeva.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request,'vastrabarana.html',context)

def pushpalankara(request):
    data = PushpalankaraSeva.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request,'pushpalankara.html',context)

def annadana(request):
    data = AnnadanaSeva.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request,'annadana.html',context)

def abhisheka(request):
    data = AbhishekaSeva.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request,'bhisheka.html',context)

def naivedya(request):
    data = NaivedyaSeva.objects.all().values()
    context = dict()
    context['data'] = data
    return render(request,'naivedya.html',context)
