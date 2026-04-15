from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.

def todolist(request):
    tareas = Tarea.objects.all().order_by('-id')
    
    return render (request, 'todolist/index.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == "POST":
        # Mandar los datos del formulario 
        form = TareaForm(request.POST)
        # Verificar que los campos son validos
        if form.is_valid():
            # Guardar en la base de datos
            form.save()
            return redirect('tareas')
    else:
        # Renderizar el formulario vacio
        form = TareaForm()

    return render(request, 'todolist/crear_tarea.html', {'form': form})