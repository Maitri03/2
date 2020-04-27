from django.contrib import admin
from django.urls import path
from .views import home, author, book, review, what_next


urlpatterns = [
    path('home/', home , name='home'),
    path('author/', author, name='author'),
    path('book', book, name='book'),
    path('review', review, name='review'),
    path('next', what_next, name='next')
]