from django.contrib import admin
from .models import Texto, Comment

# Register your models here.

@admin.register(Texto)
class TextoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido')
    search_fields = ('contenido',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha')
    search_fields = ('nombre', 'correo', 'fecha')
    list_filter = ('fecha',)
