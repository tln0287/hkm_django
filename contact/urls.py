from .views import contact
from django.urls import path, include

urlpatterns = [
    path('contact', contact, name='contact'),

]