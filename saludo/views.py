from django.http import HttpResponse
from django.shortcuts import render
from todolist.models import Tarea

# En views va toda la logica de la aplicacion

def saludo(request):
    tareas = Tarea.objects.all()

    # Renderiza un html con el saludo
    return render(request, "saludo/saludo.html", {"tareas": tareas})

def despedir(request):

    # Renderiza un html con la despedida
    return render(request, "saludo/despedir.html")

def inicio(request):
    # Renderiza un html con el inicio
    return render(request, "saludo/inicio.html")