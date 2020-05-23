from django.contrib import admin
from .models import Post, Contatos
# Register your models here.

# Fazer uma classe que herda do modelAdmin
class PostAdmin(admin.ModelAdmin):
	# Lista dos campos que vai aparecer nas colunas
	list_display = ['title', 'sub_title', 'full_name', 'ativado']

	# campo de busca
	search_fields = ['title', 'sub_title']

	# Campos que poderão ser editados
	#fields = ('title', 'sub_title')

	def get_queryset(self, request):
		return Post.objects.filter(ativado=True)

# Agora passamos também a classe que será adaptada para o Admin
admin.site.register(Post, PostAdmin)
admin.site.register(Contatos)