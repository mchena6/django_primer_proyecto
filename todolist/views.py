from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Tarea

# Create your views here.

def todolist(request):
    #tareas = Tarea.objects.all()
    #tareas = Tarea.objects.first()
    tareas = Tarea.objects.filter(completada=False)
    return HttpResponse(tareas)
