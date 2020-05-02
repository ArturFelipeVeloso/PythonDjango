from django.contrib import admin
from .models import Post
# Register your models here.

# Fazer uma classe que herda do modelAdmin
class PostAdmin(admin.ModelAdmin):
	# Lista dos campos que vai aparecer nas colunas
	list_display = ['title', 'sub_title', 'full_name']

	# campo de busca
	search_fields = ['title', 'sub_title']

	# Campos que poderão ser editados
	#fields = ('title', 'sub_title')

# Agora passamos também a classe que será adaptada para o Admin
admin.site.register(Post, PostAdmin)