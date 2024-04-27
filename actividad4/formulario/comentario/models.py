from django.db import models

class Texto(models.Model):
    contenido = models.TextField()

    def __str__(self):
        return self.contenido[:50]

class Comment(models.Model):
    texto = models.ForeignKey(Texto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.texto}"
