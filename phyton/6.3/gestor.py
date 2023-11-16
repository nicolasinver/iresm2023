"""
*   Tener un menu con 4 opciones: (GestorPeliculas)
    1. Crear una pelicula y guardar el objeto en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
"""
from peliculas import Pelicula
class GestorPeliculas:
    def __init__(self):
        self.lista_peliculas : list[Pelicula] = []
        #self.lista_peliculas = []
    
    def crear_pelicula(self):
        nombre = input('Ingrese el nombre: ')
        anio = input('Ingrese el año: ')
        genero = input('Ingrese el genero: ')
        nacionalidad = input('Ingrese la nacionalidad: ')
        puntuacion = input('Ingrese la puntuacion: ')
        pelicula = Pelicula(nombre,anio,genero,nacionalidad,puntuacion)
        self.lista_peliculas.append(pelicula)
    
    def verificar_pelicula(self):
        nombre = input('Indique el nombre de la pelicula a verificar: ')
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:
                print(f'La pelicula {nombre} existe en la lista!!!')
    
    def pedir_peliculas_anio(self):
        anio = input('Indique el año las peliculas: ')
        for pelicula in self.lista_peliculas:
            if anio == pelicula.año:
                print(pelicula.nombre)
    
    def presentar_pelicula(self):
        nombre = input('Indique el nombre de la pelicula a verificar: ')
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:
                pelicula.mostrar_info()
    
    def cambiar_genero(self):
        nombre = input('Indique el nombre de la pelicula a cambiar el genero: ')
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:
                nuevo_genero = input('Indique el nuevo genero: ')
                pelicula.cambiar_genero(nuevo_genero)  