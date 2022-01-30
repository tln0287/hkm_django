from django.shortcuts import render
from .models import Festivals

# Create your views here.
def festival(request):
    fest = Festivals.objects.all().values()
    context = dict()
    context['fest'] = fest
    return render(request,'events-list.html',context)


def event(request,id):
    fid = id
    fest = Festivals.objects.filter(id=fid).values()
    festdata = Festivals.objects.all().values()
    context = dict()
    context['fest'] = fest
    context['festdata'] = festdata
    return render(request, 'events-details.html', context)