"""Ejercicio 6.3
Crear una clase de Peliculas:

Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
Se deben crear 4 metodos en la clase:
Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion} y fue filmada en {nacionalidad}
Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
Cambiar el genero de una pelicula
Modificar puntuacion de la pelicula (entre 1 y 10)
El programa debe:

Tener un menu con 4 opciones: (GestorPeliculas)
Crear una pelicula y guardar el objeto en una lista de peliculas.
Verificar si la pelicula deseada existe en la lista de peliculas.
Pedir a la lista de peliculas, todas las de un año.
Presentar una pelicula de la lista
Cambiar el genero de una pelicula"""

class Pelicula:
    def __init__(self, nombre, año, genero, nacionalidad, puntuacion):
        self.nombre = nombre
        self.año = año
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion

    def mostrar_info(self):
        print(f"La pelicula {self.nombre} de {self.genero} del {self.año} obtuvo una puntuacion de {self.puntuacion} y fue filmada en {self.nacionalidad}")
    
    def retornar_anio(self, anio):
        if self.año < anio:
            return "Es menor al pasado por parametro"
        elif self.año == anio:
            return "Es igual al pasado por parametro"
        elif self.año > anio:
            return "Es mayor al pasado por parametro"
        else:
            return "Algo fallo"
        
    def cambiar_genero(self, genero):
        self.genero = genero

    def modificar_puntuacion(self):
        nueva_puntuacion = int(input("dame la nueva puntuacion: "))
        if 11>nueva_puntuacion>-1:
            self.puntuacion = nueva_puntuacion
        else:
            print("puntuacion invalida...")


auto.

    