from django.shortcuts import render
from .models import *
from About.models import *
from festivals.models import Festivals
from activities.models import Activities
from Gallery.models import Gallery

# Create your views here.

def index(request):
    slider = Slides.objects.all().values()
    about = AboutUs.objects.all().values()
    fest = Festivals.objects.all().values()
    activity = Activities.objects.all().values()
    gallery = Gallery.objects.all().values()

    context = dict()
    context['slider'] = slider
    context['about'] = about
    context['fest'] = fest
    context['activity'] = activity
    context['gallery'] = gallery
    return render(request,'index.html',context)
