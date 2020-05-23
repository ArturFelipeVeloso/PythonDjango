from django.contrib import admin
from django.urls import path, include

from .views import hello_blog, post_detalhes, contatos, sobre

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/contatos
# http://127.0.0.1:8000/sobre
# http://127.0.0.1:8000/post/1

urlpatterns = [
    path('', hello_blog, name = 'index'),
    path('post/<int:id>', post_detalhes, name = 'post_detalhes'),
    path('contatos/', contatos, name = 'contatos'),
    path('sobre/', sobre, name = 'sobre'),
]