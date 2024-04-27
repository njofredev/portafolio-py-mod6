from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User  # Importa el modelo de usuario

# Obtener el usuario (por ejemplo, el primer usuario)
user = User.objects.first()

# Crear grupos si no existen
group, created = Group.objects.get_or_create(name='Admins')
if created:
    # Obtener los permisos necesarios
    content_type = ContentType.objects.get_for_model(Permission)
    perm = Permission.objects.filter(content_type=content_type)
    group.permissions.set(perm)

# Asignar un usuario a un grupo
user.groups.add(group)
