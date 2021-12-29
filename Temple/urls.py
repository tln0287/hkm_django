from .views import templehistory
from django.urls import path, include

urlpatterns = [
    path('templehistory', templehistory, name='templehistory'),
]