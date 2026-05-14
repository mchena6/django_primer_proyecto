from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)  # Permite modificar el uso de la clase User por defecto

# Create your models here.


# Modelo User (campos por defecto)+ campos personalizados
class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to="users_fp/", blank=True, null=True)
    dni = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.dni}"
