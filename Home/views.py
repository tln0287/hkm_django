from django.shortcuts import render
from .models import *
from About.models import *
from festivals.models import Festivals

# Create your views here.

def index(request):
    slider = Slides.objects.all().values()
    about = AboutUs.objects.all().values()
    fest = Festivals.objects.all().values()

    context = dict()
    context['slider'] = slider
    context['about'] = about
    context['fest'] = fest
    return render(request,'index.html',context)
