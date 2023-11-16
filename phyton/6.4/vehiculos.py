"""Ejercicio 6.4
Crear una clase padre Vehiculos:

Constructor debe incluir los atributos (patente,marca,año,origen)
Crear metodos para esta clase de:
Presentarse (patente,marca,año,origen)
Indicar tipos de vehiculo(Clases heredadas)
Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una

Particular
PickUp
Deportivo
Crear clase GestorAutos que cuente con las siguientes funciones para un menu

Crear auto, indicando tipo de auto y guardar en una lista
Listar autos (presentandolos), indicando tipo de Vehiculo.
Cambiar velocidad de un Vehiculo
Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)"""

class Vehiculos:
    def __init__(self,patente,marca,año,origen,velocidad):
        self.patente = patente
        self.marca = marca 
        self.año = año
        self.origen = origen
        self.velocidad = velocidad


    def presentacion(self):
        print(f"mi patente es {self.patente} soy un {self.marca} del año {self.año} y de origen {self.origen}")

    def tipo_auto(self):
        print("Soy un auto del tipo", type(self).__name__)

class particular(Vehiculos):
    def __init__(self,patente,marca,año,origen,velocidad,ruedas):
        super().__init__(patente,marca,año,origen,velocidad)
        self.ruedas = ruedas
    

class pickup(Vehiculos):
    def __init__(self,patente,marca,año,origen,velocidad,asientos):
        super().__init__(patente,marca,año,origen,velocidad)
        self.asientos = asientos

class deportivo(Vehiculos):
    def __init__(self,patente,marca,año,origen,velocidad, puertas):
        super().__init__(patente,marca,año,origen,velocidad)
        self.puertas = puertas

