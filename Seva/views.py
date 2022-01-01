from django.shortcuts import render

# Create your views here.
def vastrabarana(request):
    return render(request,'vastrabarana.html')

def pushpalankara(request):
    return render(request,'pushpalankara.html')

def annadana(request):
    return render(request,'annadana.html')

def bhisheka(request):
    return render(request,'bhisheka.html')

def naivedya(request):
    return render(request,'naivedya.html')
