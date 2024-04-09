from django.shortcuts import render
from .models import Saludo

def index(request):
  saludo = Saludo.objects.first()
  if saludo:
      contexto = {'mensaje': saludo.mensaje}
  else:
      contexto = {'mensaje': "No hay saludos guardados aún"}  # Mensaje predeterminado
  return render(request, 'templates/index.html', contexto)