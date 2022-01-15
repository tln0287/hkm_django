from .views import *
from django.urls import path, include

urlpatterns = [
    path('annadana', annadana, name='annadana'),
    path('vastrabarana', vastrabarana, name='vastrabarana'),
    path('pushpalankara', pushpalankara, name='pushpalankara'),
    path('abhisheka', abhisheka, name='abhisheka'),
    path('naivedya', naivedya, name='naivedya'),

]