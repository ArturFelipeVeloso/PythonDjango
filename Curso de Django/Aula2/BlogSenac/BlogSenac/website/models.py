from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=80)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    texto = models.TextField()

    imagem = models.ImageField(upload_to = 'posts', null = True, blank = True)

    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    status = models.CharField(max_length=10,
                              choices = STATUS,
                              default = 'rascunho'
                             )

    CATEGORIAS = (
        ('programacao', 'Programação'),
        ('eletronica', 'Eletrônica')
    )

    categorias = models.CharField(max_length=12,
                              choices = CATEGORIAS,
                              default = 'programacao'
                             )

    publicado = models.DateTimeField(default=timezone.now())
    cadastrado = models.DateTimeField(auto_now_add = True )
    alterado = models.DateTimeField(auto_now = True)

    ativado = models.BooleanField(default = True)

    def __str__(self):
        return self.title