<div align="center">

# Proyecto Movie DataBase Application

</div>

<details>

<summary>Tabla de contenidos</summary>

- [Explicación de la aplicación](#explicación-de-la-aplicación)
- [Funcionamiento y características](#funcionamiento-y-características)
- [Descarga y ejecución](#descarga-y-ejecución)
- [Stack](#🛠️-stack)

</details>

# Explicación de la aplicación
La solución del aplicativo se dividirá en varias partes:

- Manipulación de Json
- Crear las tablas para la base de datos
- Gestionar y/o manipular el archivo Json y subida de los datos a la base de datos
- Generar las vistas para mostrar las películas y el filtrado por categoría

Lo primero a tener en cuenta para la realización del aplicativo son los datos entregados en el archivo Json, 
dicho archivo siendo tan extenso tendrá 11 datos por película siendo estos los siguientes:

- Título de la película
- Año de lanzamiento
- Genero(s)
- Calificaciones recibidas en IMBD por múltiples usuarios del 1 al 10
- Cantidad de vistas
- Argumento
- Actores
- Duración
- Fecha de publicación
- Índice de madurez
- Imagen de cartelera

**Consideraciones:**

- Revisando lo anterior nos damos cuenta que la fecha de publicación y el año de lanzamiento pueden estar contenidos en un solo campo
pues sería redundar teniendo los 2, se tomará la fecha de publicación que es más específica

- El campo de índice de madurez que en el archivo es "contentRating" contiene valores predeterminados de la siguiente manera:

### [IMAGEN  CONTENT  RATING](https://github.com/Jhonatanls/prueba-codigo/blob/main/contentRating.png)

Tomando lo anterior en cuenta debemos empezar a imaginarnos las tablas que tendrá nuestro aplicativo, surgiendo para este apartado
4 tablas o modelos principales:

- Película 
- Género de la película (Relación con pelicula de muchos a muchos)
- Actor (Relación con pelicula de muchos a muchos)
- Índice de madurez (Relación con película de uno a muchos)

De este análisis sale un diagrama entidad relación de las anteriores tablas:

### [IMAGEN  diagrama](https://github.com/Jhonatanls/prueba-codigo/blob/main/Diagrama%20ER%20de%20base%20de%20datos%20(movie_database).png)

Para la lógica que tome en cuestión de filtrar por popularidad lo hice tomando la lista rating de cada película y dividiendo entre el size de la misma, 
así me daría un numero decimal que posteriormente podría filtrar con botones.

De esta misma forma lo hice para la duración y la fecha de publicación, filtré y generé botones para que se pudiera ver el ordenamiento


# Funcionamiento y características

## Funcionamiento
Proyecto que se encargará de gestionar una base de datos que es entregada en formato Json. La aplicación permitirá a los usuarios filtrar la película por múltiples criterios como género, actor, duración, año y popularidad.

Se entra a la aplicación y se verá una tabla con las peliculas cargadas, así mismo se veran etiquetas en las que dando click se podrá filtrar ascendentemente y descendentemente.

## Características 

- **Detalles**: Esta aplicación fue desarrollada en windows con el lenguaje de programación Python y su framework Django.

# Descarga y ejecución

Para el código de este proyecto se debe clonar este repositorio en el cual se encontrará un proyecto de Django.
El proyecto principal se llama movies_database, solo se usó para entregarle todos los parametros y configuraciones necesarias
como mostrarle donde estarán los archivos estaticos, la zona horaria y las configuraciones para dockerizar el proyecto

Se creó una app que se llamo 'movies', en ella se crearon las vistas y urls para mostrar los filtros, además de esto se creo una carpeta management/command
el cual contiene un script, que se encargó de cargar los datos del archivo 'movies.json' en la base de datos

También hay una carpeta para los templates de las vistas de los filtros creados:
- Popularidad
- Fecha
- Duración
- Nombre

El proyecto será dockerizado y subido a DuckerHub con el nombre de **jhonatan25ls/movies-database:latest**
Se podrá descargar y ejecutar la imagen usando el cmd y los siguientes comandos
- docker push  jhonatan25ls/movies-database:latest
- docker run -p 8000:8000 jhonatan25ls/movies-database:latest
- Se deberá abrir localhost:8000 y la aplicación correrá

# 🛠️ Stack

- [![python][python-badge]][python-url] Lenguaje de programación.
- [![django][django-badge]][django-url] Framework web.

[python-url]: https://www.python.org/
[python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[django-url]: https://www.djangoproject.com/
[django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
