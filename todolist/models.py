from django.db import models
# Importar usuarios
from django.contrib.auth.models import User

# El id se crea automaticamente

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"Soy la etiqueta: {self.nombre}"

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completada = models.BooleanField(
        default=False,
        help_text="La tarea esta completada?",
        verbose_name="Tarea finalizada"    
    )
    fecha_completado = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    # Campo relacionado a un usuario
    responsable = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="responsable", 
        default=None, 
        blank=True,
        null=True
        )
    # Para ver el responsable de una tarea, se puede usar: tarea.responsable
    etiqueta = models.ManyToManyField(
        Etiqueta, 
        related_name="etiqueta", 
        default=None, 
        blank=True)
    activo = models.BooleanField(default=True, help_text="La tarea esta activa?")
    imagen = models.ImageField(upload_to='card_image/', null=True, blank=True)

    # Funcion para mostrar el nombre de la tarea en mayuscula (no se guarda en la base de datos)
    def nombre_mayuscula(self):
        return f"{self.nombre.upper()}"
    
    
    def __str__(self):
        return f"Soy la tarea: {self.nombre}"
    
    class Meta:
        verbose_name = "Tarea de proyecto"
        verbose_name_plural = "Tareas de proyecto"
        ordering = ["-id"]