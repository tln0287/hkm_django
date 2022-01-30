from django.shortcuts import render
from .models import Activities

# Create your views here.
def activity(request):
    fest = Activities.objects.all().values()
    context = dict()
    context['fest'] = fest
    return render(request,'activitylist.html',context)


def activitydetail(request,id):
    fid = id
    fest = Activities.objects.filter(id=fid).values()
    festdata = Activities.objects.all().values()
    context = dict()
    context['fest'] = fest
    context['festdata'] = festdata
    return render(request, 'activitydetails.html', context)