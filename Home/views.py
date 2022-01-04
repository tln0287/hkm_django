from django.shortcuts import render
from .models import *
from About.models import *

# Create your views here.

def index(request):
    slider = Slides.objects.all().values()
    about = AboutUs.objects.all().values()

    context = dict()
    context['slider'] = slider
    context['about'] = about
    return render(request,'index.html',context)
