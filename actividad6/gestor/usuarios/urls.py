from django.urls import path
from . import views

urlpatterns = [
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('crear_grupo/', views.crear_grupo, name='crear_grupo'),
    path('lista_grupos/', views.lista_grupos, name='lista_grupos'),
    path('eliminar_grupo/<int:grupo_id>/', views.eliminar_grupo, name='eliminar_grupo'),
    path('modificar_usuario/<int:usuario_id>/', views.modificar_usuario, name='modificar_usuario'),
    path('editar_grupo/<int:grupo_id>/', views.editar_grupo, name='editar_grupo'),
]
