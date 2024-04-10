from django.core.management.base import BaseCommand
from movies.models import Pelicula, Genero, Indice_madurez, Actor
import json
import os

current_dir = os.path.dirname(__file__)
json_file_path = os.path.join(current_dir, 'movies.json')

class Command(BaseCommand):
    help = 'Load a movies JSON file into the database'

    def handle(self, *args, **kwargs):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            movies_json = json.load(file)

            for movie_data in movies_json:
                # Crear o obtener géneros
                genero = [Genero.objects.get_or_create(name=genero_name)[0] for genero_name in movie_data['genres']]
                # Crear o obtener actores
                actor = [Actor.objects.get_or_create(name=actor_name)[0] for actor_name in movie_data['actors']]
                # Crear o obtener indices
                indice = [Indice_madurez.objects.get_or_create(name=indice_name)[0] for indice_name in movie_data['contentRating']]

            for movie_data in movies_json:
                duracion_no_format = str(movie_data['duration'])
                calificacion_no_format=list(movie_data['ratings'])
                pelicula = Pelicula(
                    titulo=movie_data['title'],
                    fecha_publicacion=movie_data['releaseDate'],
                    cantidad_vistas=movie_data['viewerCount'],
                    argumento=movie_data['storyline'],
                    duracion=int(duracion_no_format[2:len(duracion_no_format)-1]),
                    calificacion=sum(calificacion_no_format)/len(calificacion_no_format)
                )
                pelicula.save()
                # Añadir géneros, actores e indices a la película
                pelicula.genero.set(genero)
                pelicula.actor.set(actor)
                pelicula.indice_madurez.set(indice)
                
    
