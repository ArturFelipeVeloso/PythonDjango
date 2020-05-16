from django.contrib import admin
from django.urls import path, include

from .views import hello_blog, post_detalhes

# http://127.0.0.1:8000/blog/
# http://127.0.0.1:8000/blog/post/1

urlpatterns = [
    path('', hello_blog),
    path('post/<int:id>', post_detalhes, name = 'post_detalhes'),
]