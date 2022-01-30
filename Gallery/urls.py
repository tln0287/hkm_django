from .views import gallery, weekly_darshan, festival_darshan,media,videos
from django.urls import path, include

urlpatterns = [
    path('gallery', gallery, name='gallery'),
    path('weekly_darshan', weekly_darshan, name='weekly_darshan'),
     path('festival_darshan', festival_darshan, name='festival_darshan'),
    path('media', media, name='media'),
    path('videos', videos, name='videos'),

]
