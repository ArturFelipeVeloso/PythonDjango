from django.urls import path, include
from .views import hello_blog, post_detalhes, contatos, sobre

urlpatterns = [
    path('', hello_blog, name = 'postagens'),
    path('post/<int:id>/', post_detalhes, name = 'post_detalhes'),
    path('sobre/', sobre, name = 'sobre'),
    path('contatos/', contatos, name = 'contatos'),
    path('salvar-form/', contatos, name = 'contatos'),
]
