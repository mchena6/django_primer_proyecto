# Ruta donde van los endpoints de la aplicacion

from django.urls import path, include

# Importamos las vistas para poder usarlas en las rutas
from . import views

# Variable para conectar las rutas con las vistas
# Ruta, view, nombre de la ruta para usarla en el html
urlpatterns = [
    path('', views.todolist, name="tareas"),
    path("nueva/", views.crear_tarea, name="crear_tarea")
]