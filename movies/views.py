from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Pelicula

def listar_peliculas(request):
    orden = request.GET.get('orden', 'asc')
    if orden == 'desc':
        peliculasListadas = Pelicula.objects.all().order_by('-titulo')
    else:
        peliculasListadas = Pelicula.objects.all().order_by('titulo')

    paginator = Paginator(peliculasListadas, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "movies/gestionPeliculas.html", {"page_obj": page_obj})

def listar_popularidad(request):

    orden = request.GET.get('orden', 'asc')
    if orden == 'desc':
        peliculasListadas = Pelicula.objects.all().order_by('-calificacion')
    else:
        peliculasListadas = Pelicula.objects.all().order_by('calificacion')

    paginator = Paginator(peliculasListadas, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "movies/gestionPopularidad.html", {"page_obj": page_obj})

def listar_duracion(request):
    orden = request.GET.get('orden', 'asc')
    if orden == 'desc':
        peliculasListadas = Pelicula.objects.all().order_by('-duracion')
    else:
        peliculasListadas = Pelicula.objects.all().order_by('duracion')

    paginator = Paginator(peliculasListadas, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "movies/gestionDuracion.html", {"page_obj": page_obj})

def listar_fecha(request):
    orden = request.GET.get('orden', 'asc')
    if orden == 'desc':
            peliculasListadas = Pelicula.objects.all().order_by('-fecha_publicacion')
    else:
        peliculasListadas = Pelicula.objects.all().order_by('fecha_publicacion')

    paginator = Paginator(peliculasListadas, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "movies/gestionFecha.html", {"page_obj": page_obj})