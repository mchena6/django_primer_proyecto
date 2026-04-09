from django.contrib import admin
from .models import Tarea, Etiqueta


# Register your models here.
admin.site.register(Etiqueta)

# Funcion para personalizar el admin de tareas
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    # Columnas
    list_display = ("id", "nombre", "completada", "fecha_completado","fecha_creacion", "responsable")
    # Columna para filtrar
    list_filter = ("completada",)
    # Barra de busqueda
    search_fields = ("nombre",)
    # Campos que no se pueden modificar
    readonly_fields = ("completada",)
