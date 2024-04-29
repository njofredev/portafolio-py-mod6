from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Define la clase de administrador personalizado para el modelo User
class CustomUserAdmin(UserAdmin):
    # Campos que se muestran en la lista de usuarios en el panel de administración
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Campos que se pueden buscar en la lista de usuarios en el panel de administración
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Campos que se pueden filtrar en la lista de usuarios en el panel de administración
    list_filter = ('is_staff', 'is_superuser', 'groups')

# Desregistrar el modelo User de su administrador predeterminado
admin.site.unregister(User)

# Registrar el modelo User con el administrador personalizado
admin.site.register(User, CustomUserAdmin)
