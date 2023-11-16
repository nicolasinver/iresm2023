'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 APELLIDO Y NOMBRE: 
 DNI: 
 CARRERA: 
 ************************************************************
 Ítems a evaluar:
 1. Contenidos de la materia
 2. Requerimientos y comprensión de consignas
 3. Estructura (modularización), legibilidad y comentarios del código.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de gestion de hoteles"

Introducción: 
    El siguiente programa consiste en un software que simule una programa para gestionar las habitatociones de un hotel.
    El programa debe permitir agregar y quitar habitaciones al sistema, como también gestionar datos del estas (numero, max_personas, precio).

Requerimientos:
El programa debe:
*   Contar con una Clase Habitacion con los atributos (numero (único), max_pesonas (int), precio (float))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - HabitacionClasica (Atributo: cant_televisores (int))
        - HabitacionPremium (Atributo: Jacuzzi "True o False" (por defecto = True))
        
*   Se deben crear los siguientes métodos para la clase padre Habitacion (que heredaran las clases hijas):
        1. Mostrar información: Que indique el numero, max_personas y precio
           -  Este metodo debe ser creado en la clase padre y las hijas, ya que las clases hijas deben mostrar tambien sus atributos
        2. Setear y obtener max_personas
        3. Setear y obtener precio
        4. Obtener tipo de clase

*   Se debe crear una clase GestorHabitaciones que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de una habitacion y guárdalos en una lista de habitaciones. 
        1.1) Se debe verificar que tipo de instancia de Habitacion a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - numero: debe ser único
             - max_personas: verificar que sea un numero entero y este entre 2 y 6 inclusives.
             - precio: se debe pedir en pesos pero se debe guardar en dolares (1 dolar -> 900 pesos)
        1.2) Clases hijas:
             - cant_televisores: verificar que sea entero entre 0 y 3 incluses
             - Jacuzzi: verificar que sea True o False (boolean)
             
        1.3) Al crear una Habitacion es necesario logearlo (Escribir en una línea nueva: numero,max_personas,precio,tipo_de_clase)) 
             en un archivo llamado historial_habitaciones.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos y extension
    2.   Cambiar precio de habitacion, seleccionando su numero: Se debe cambiar el precio de la habitacion dependiendo de la cant max de 
         personas que contenga y el tipo de habitacion:
         - Se debe leer el diccionario por el tipo de habitacion y multiplicar ese precio por la cantidad de personas.
         Ej. Precio hab clasica = 400 (CL)* max_personas = 400 * 5 = 2000 IMPORANTE! solo se le pide el numero de habitacion al usuario
    3.   Pedir al usuario un numero y listar esa cantidad de habitaciones de la lista, verificando que hayan esa cantidad de habitaciones
    
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

class Habitacion:
    def __init__(self,numero,maxPersonas,precio):
        self.numero = numero
        self.maxPersonas = maxPersonas
        self.precio = precio
    
    def imprimirInfo(self):
        print(f"Habitacion numero: {self.numero} Maximo de Personas: {self.maxPersonas} Precio: {self.precio}")
    
    def setear_max_personas(self,personas):
        self.maxPesonas = personas
    
    def setear_precio(self,precio):
        self.precio = precio
    
    def get_max_personas(self):
        return self.maxPesonas

    def get_precio(self):
        return self.precio
    
    def tipo_habitacion(self):
        print("Soy una habitacion del tipo", type(self).__name__)
        return type(self).__name__
    
class comun(Habitacion):
    def __init__(self,numero,maxPersonas,precio):
        super.__init__(self,numero,maxPersonas,precio)

class Clasica(Habitacion):
    def __init__(self,numero,maxPersonas,precio,televisores:int):
        super.__init__(self,numero,maxPersonas,precio)
        self.televisores = televisores

    def imprimirInfo(self):
        print(f"Habitacion numero: {self.numero} Maximo de Personas: {self.maxPersonas} Precio: {self.precio} Televisores: {self.televisores}")

class Premium(Habitacion):
    def __init__(self,numero,maxPersonas,precio,jacuzzi=True):
        super.__init__(self,numero,maxPersonas,precio)
        self.jacuzzi = jacuzzi
    
    def imprimirInfo(self):
        print(f"Habitacion numero: {self.numero} Maximo de Personas: {self.maxPersonas} Precio: {self.precio} jacuzzi: {self.jacuzzi}")