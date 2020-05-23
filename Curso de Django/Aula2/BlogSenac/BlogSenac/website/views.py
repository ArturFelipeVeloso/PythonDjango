from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def hello_blog(request):
	lista = [
		'Python', 'HTML', 'CSS', 'JS', 'PyCharm', 'Ruby'
	]

	#ListaDePosts = Post.objects.all()
	ListaDePosts = Post.objects.filter(ativado=True)

	dados = {
		'Nome' : 'Curso de Django',
		'Areas' : lista,
		'Posts': ListaDePosts
	}

	return render(request, 'index.html', dados)

def post_detalhes(request, id):
	post = Post.objects.get(id=id)

	data = {
		'Postagem': post
	}

	return render(request, 'postagem.html', data)

def sobre(request):
	return render(request, 'sobre.html')

def contatos(request):
	return render(request, 'contatos.html')