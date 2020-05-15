from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def hello_blog(request):
	lista = [
		'Python', 'HTML', 'CSS', 'JS', 'PyCharm', 'Ruby'
	]

	ListaDePosts = Post.objects.all()

	dados = {
		'Nome' : 'Curso de Django',
		'Areas' : lista,
		'Posts': ListaDePosts
	}

	return render(request, 'index.html', dados)