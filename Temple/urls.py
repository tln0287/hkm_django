from .views import templehistory,facilities,guesthouse
from django.urls import path, include

urlpatterns = [
    path('templehistory', templehistory, name='templehistory'),
    path('facilities', facilities, name='facilities'),
    path('guesthouse', guesthouse, name='guesthouse'),
]