from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from .forms import UserForm, GroupForm

def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # Redirige a la lista de usuarios
    else:
        form = UserForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

def eliminar_usuario(request, usuario_id):
    user = User.objects.get(pk=usuario_id)
    user.delete()
    return redirect('lista_usuarios')  # Redirige a la lista de usuarios

def crear_grupo(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')  # Redirige a la lista de grupos
    else:
        form = GroupForm()
    return render(request, 'usuarios/crear_grupo.html', {'form': form})

def eliminar_grupo(request, grupo_id):
    group = Group.objects.get(pk=grupo_id)
    group.delete()
    return redirect('lista_grupos')  # Redirige a la lista de grupos


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


def modificar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # Redirige a la lista de usuarios
    else:
        form = UserForm(instance=usuario)
    return render(request, 'usuarios/modificar_usuario.html', {'form': form})

def lista_grupos(request):
    grupos = Group.objects.all()
    return render(request, 'usuarios/lista_grupos.html', {'grupos': grupos})


def editar_grupo(request, grupo_id):
    grupo = get_object_or_404(Group, pk=grupo_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')  # Redirige a la lista de grupos
    else:
        form = GroupForm(instance=grupo)
    return render(request, 'usuarios/editar_grupo.html', {'form': form})
