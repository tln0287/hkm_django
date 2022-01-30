from .views import contact,contactquery
from django.urls import path, include

urlpatterns = [
    path('contact', contact, name='contact'),
    path('contactquery', contactquery, name='contactquery'),

]