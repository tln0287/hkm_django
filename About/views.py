from django.shortcuts import render
from .models import AboutUs, Team
# Create your views here.

def about(request):
    about = AboutUs.objects.all().values()
    team = Team.objects.all().values()
    context = dict()
    context['title'] = about[0]['title']
    context['content'] = about[0]['content']
    context['about_img'] = about[0]['about_image']
    context['team'] = team
    return render(request,'about.html', context)
