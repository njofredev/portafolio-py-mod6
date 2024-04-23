from django.db import models
from django.utils import timezone


class Post(models.Model):
    TituloPost = models.CharField(max_length=200)
    Contenido = models.TextField()
    FechaPost = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.TituloPost
