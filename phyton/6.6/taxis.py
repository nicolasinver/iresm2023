"""Ejercicio 6.6 (Empresa de Taxis)
Simular una empresa de taxis que cuente con dos clases: Autos y Chofer

La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))

La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)

Contar con 6 funciones disponibles en el menu (estas funciones deben estar incluidas en una clase llamada GestorTaxis):

Crear instancias de choferes y guardarlos en una lista de choferes
Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
Modificar el chofer de un auto
Modificar el lugar de residencia del chofer indicando su nombre
imprmiir lista de choferes (con toda su informacion)
imprimir lista de autos (con toda su informacions)
Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes

Gestionar posibles errores

Estructurar el programa a criterio propio"""

class autos:
    def __init__(self,patente, modelo, año, marca, nombre_Chofer):
        self.patente = patente
        self.modelo = modelo
        self.año = año
        self.marca = marca
        self.nombre_Chofer = nombre_Chofer


class chofer:
    def __init__(self,nombre, apellido, dni, fecha_nacimiento, Residencia):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.Residencia = Residencia