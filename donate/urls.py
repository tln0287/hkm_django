from .views import donate,donatenow,add_donation,charged
from django.urls import path, include

urlpatterns = [
    path('donate', donate, name='donate'),
    path('add_donation', add_donation, name='add_donation'),
    path('charged', charged, name='charged'),
    path('donatenow/<int:id>/', donatenow, name='donatenow'),

]