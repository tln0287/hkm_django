from .views import gallery
from django.urls import path, include

urlpatterns = [
    path('gallery', gallery, name='gallery'),

]