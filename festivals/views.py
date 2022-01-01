from django.shortcuts import render

# Create your views here.
def festival(request):
    return render(request,'events-list.html')