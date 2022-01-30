from django.shortcuts import render
from .models import Gallery, WeeklyDarshan,FestivalDarshan,Media,Videos

# Create your views here.
def gallery(request):
    gallery = Gallery.objects.all().values()
    context = dict()
    context['gallery'] = gallery
    return render(request,'gallery.html',context)

def weekly_darshan(request):
    gallery = WeeklyDarshan.objects.all().values()
    context = dict()
    context['gallery'] = gallery
    return render(request,'weekly-darshan.html',context)

def festival_darshan(request):
    gallery = FestivalDarshan.objects.all().values()
    context = dict()
    context['gallery'] = gallery
    return render(request,'festival-darshan.html',context)

def media(request):
    gallery = Media.objects.all().values()
    context = dict()
    context['gallery'] = gallery
    return render(request,'media.html',context)

def videos(request):
    gallery = Videos.objects.all().values()
    context = dict()
    context['youtube_links'] = gallery
    return render(request,'videos.html',context)