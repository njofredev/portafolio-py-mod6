from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("TituloPost", "FechaPost")
    search_fields = ("TituloPost", "Contenido")
    list_filter = ("FechaPost",)
