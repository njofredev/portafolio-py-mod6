from django.contrib import admin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')  # Muestra el título y el ID del artículo en la interfaz de administración

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created_at')  # Muestra el nombre del autor del comentario, el artículo al que pertenece y la fecha de creación
