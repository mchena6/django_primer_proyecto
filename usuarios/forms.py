from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado


class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        # Modelo base + campos personalizados del modelo UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + (
            "telefono",
            "foto_perfil",
            "dni",
        )
