from django.contrib import admin
from .models import TuModelo

@admin.register(TuModelo)
class TuModeloAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'Direccion')

