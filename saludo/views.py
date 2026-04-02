from django.http import HttpResponse
from django.shortcuts import render

# En views va toda la logica de la aplicacion

# Le pasamos variables al html
contexto = {
    "nombre": "Mundo",
    "esMayor": True,
    "mascotas": ["Perro", "Gato", "Pez"]
}

def saludo(request):

    # Renderiza un html con el saludo
    return render(request, "saludo/saludo.html", contexto)

def despedir(request):

    # Renderiza un html con la despedida
    return render(request, "saludo/despedir.html", contexto)

def inicio(request):
    # Renderiza un html con el inicio
    return render(request, "saludo/inicio.html", contexto)