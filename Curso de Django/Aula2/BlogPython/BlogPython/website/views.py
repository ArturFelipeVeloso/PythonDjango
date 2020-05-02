from django.shortcuts import render
from .models import Post

def hello_blog(request):
	lista = [
		'Python', 'Inteligência Artificial', 'GIT', 'PyCharm',
		'Máquina Virtual', 'Anacondas', 'Django', 'HTML'
	]

	list_posts = Post.objects.all()

	data = {'Name':'Curso de Django Senac',
	        'areas':lista,
	        'posts':list_posts}

	return render(request, 'index.html', data)