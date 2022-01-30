from .views import archana,lectures,books,biography,bhajana,bbooks
from django.urls import path, include

urlpatterns = [
    path('archana', archana, name='archana'),
    path('lectures', lectures, name='lectures'),
    path('books', books, name='books'),
    path('bbooks', bbooks, name='bbooks'),
    path('biography', biography, name='biography'),
    path('bhajana', bhajana, name='bhajana'),

]