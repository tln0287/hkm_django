from .views import about
from django.urls import path, include

urlpatterns = [
    path('about', about, name='about'),

]