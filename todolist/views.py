from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm


def todolist(request):
    tareas = Tarea.objects.filter(activo=True)
    
    return render (request, 'todolist/index.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == "POST":
        # Mandar los datos del formulario Y los archivos (imagenes)
        form = TareaForm(request.POST, request.FILES)
        # Verificar que los campos son validos
        if form.is_valid():
            # Guardar en la base de datos
            form.save()
            return redirect('tareas')
    else:
        # Renderizar el formulario vacio
        form = TareaForm()

    return render(request, 'todolist/crear_tarea.html', {'form': form})

# Parametro Ruta: url.com/editar_tarea/<id>
def editar_tarea(request, id):
    # Obtener tarea
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == "POST":
        form = TareaForm(request.POST, request.FILES, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:   
        # Renderizar el formulario con los datos de la tarea
        form = TareaForm(instance=tarea)
    return render(request, "todolist/editar_tarea.html", {"form": form})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    # Borrado logico
    if request.method == "POST":
        tarea.activo = False
        # Guardar el cambio en la base de datos
        tarea.save()
        return redirect('tareas')
    return render(request, "todolist/borrar_tarea.html", {"tarea": tarea})
