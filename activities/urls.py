from .views import activity, activitydetail
from django.urls import path, include

urlpatterns = [
    path('activity', activity, name='activity'),
    path('activitydetail/<int:id>', activitydetail, name='activitydetail'),

]