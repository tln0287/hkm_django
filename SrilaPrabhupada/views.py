from django.shortcuts import render

# Create your views here.
def archana(request):

    return render(request, 'archana.html')

def biography(request):
    return render(request, 'biography.html')

def books(request):
    return render(request, 'books.html')

def lectures(request):
    return render(request, 'lectures.html')

def bhajana(request):
    return render(request, 'bhajana.html')
