# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso

# Create your views here.

def Home(request):
    CursosListado = Curso.objects.all() 
    # return HttpResponse ('<h1> bienvenidos a la pagina de inicio </h1>')
    # CursosListado = Curso.objects.filter(calificacion = 8)
    # CursosListado = Curso.objects.filter(calificacion__gte = 8)
    # CursosListado = Curso.objects.filter(calificacion__lte = 6)                             
    
    data = {
        'titulo': 'Gestion de Cursos',
        'cursos': CursosListado
    }
    return render(request, 'GestionCursos.html', data)

class CursoListView(ListView):
    model = Curso
    template_name = "GestionCursos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Cursos'
        return context