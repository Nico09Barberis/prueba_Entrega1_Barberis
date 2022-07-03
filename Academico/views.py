# from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.

def Home(request):
    CursosListado = Curso.objects.all() 
    # return HttpResponse ('<h1> bienvenidos a la pagina de inicio </h1>')
    # CursosListado = Curso.objects.filter(calificacion = 8)
    # CursosListado = Curso.objects.filter(calificacion__gte = 8)
    # CursosListado = Curso.objects.filter(calificacion__lte = 6)                             
    return render(request, 'GestionCursos.html', {'cursos': CursosListado})