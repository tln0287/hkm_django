from .views import festival
from django.urls import path, include

urlpatterns = [
    path('festival', festival, name='festival'),

]