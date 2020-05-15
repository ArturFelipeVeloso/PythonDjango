from django.contrib import admin
from django.urls import path, include

from .views import hello_blog

# http://127.0.0.1:8000/blog/

urlpatterns = [
    path('', hello_blog),
]