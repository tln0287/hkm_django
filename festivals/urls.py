from .views import festival,event
from django.urls import path, include

urlpatterns = [
    path('festival', festival, name='festival'),
    path('event/<int:id>', event, name='event'),

]