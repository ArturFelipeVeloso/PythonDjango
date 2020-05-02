from django.db import models

# models é um pacote que já está pronto no django
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    # Quando solicitar este objeto, será retornado o titulo ao inves do objeto em si
    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    # Novidade do django 3
    # A coluna nome completa vai ser ordenada juntamente com o campo title
    full_name.admin_order_field = 'title'