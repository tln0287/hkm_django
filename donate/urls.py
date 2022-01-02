from .views import donate
from django.urls import path, include

urlpatterns = [
    path('donate', donate, name='donate'),

]