from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=80)
    texto = models.TextField()

    def __str__(self):
        return self.title