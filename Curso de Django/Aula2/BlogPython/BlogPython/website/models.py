from django.db import models

# models é um pacote que já está pronto no django



class Post(models.Model):

    class Categorias(models.TextChoices):
        PY = 'PY', 'Python'
        DJ = 'DJ', 'Django'
        PG = 'PG', 'Programação'
        IOT = 'IoT', 'Internet das Coisas'
        POO = 'POO', 'Programação Orientada a Objetos'
        BD = 'BD', 'Banco de dados'

    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado', 'Publicado')
    )

    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    imagem = models.ImageField(upload_to='posts', null=True, blank=True)

    categoria = models.CharField(max_length = 3,
                                 choices = Categorias.choices,
                                 default = Categorias.PG
                                )

    Status = models.CharField(max_length = 10,
                              choices=STATUS,
                              default = 'rascunho')

    ativado = models.BooleanField(default = True)

    # Quando solicitar este objeto, será retornado o titulo ao inves do objeto em si
    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    # Novidade do django 3
    # A coluna nome completa vai ser ordenada juntamente com o campo title
    full_name.admin_order_field = 'title'


class Contatos(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    mensagem = models.TextField()