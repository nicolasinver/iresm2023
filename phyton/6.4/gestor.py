from vehiculos import *
"""Crear clase GestorAutos que cuente con las siguientes funciones para un menu

Crear auto, indicando tipo de auto y guardar en una lista
Listar autos (presentandolos), indicando tipo de Vehiculo.
Cambiar velocidad de un Vehiculo
Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)"""

class GestorAutos:
    def __init__(self):
        self.lista_vehiculos : list[Vehiculos] = []

    def verificar_tipo_auto(self):
        while True:
            print('------ Posibles autos a crear ------')
            lista_tipos = []
            for i in Vehiculos.__subclasses__():
                print(f'- {i.__name__}')
                lista_tipos.append(i.__name__)
            tipo_clase = input('indique el auto nuevo: ')
            if tipo_clase in lista_tipos:
                return tipo_clase
            else:
                print('Esa clase no existe')

    def crear_auto(self):
        tipo_de_auto = self.verificar_tipo_auto()
        patente = input("dime su patente: ")
        marca = input("dime su marca: ")
        año = input ("dame su año: ")
        origen = input("dime su origen: ")
        velocidad = int(input("dime su velocidad: "))

        if tipo_de_auto == "particular":
            ruedas = input("dame su numero de ruedas: ")
            nuevo_auto = particular(patente,marca,año,origen,velocidad,ruedas)
        elif tipo_de_auto == "pickup":
            asientos = input("dame su numero de asientos: ")
            nuevo_auto = pickup(patente,marca,año,origen,velocidad,asientos)
        elif tipo_de_auto == "deportivo":
            puertas = input("dame su numero de puertas: ")
            nuevo_auto = deportivo(patente,marca,año,origen, velocidad, puertas)
        self.lista_vehiculos.append(nuevo_auto)

    def presentaciones(self):
        for i in self.lista_vehiculos:
            i.presentacion()
            i.tipo_auto()

    def cambiar_velocidad(self):
        for i in self.lista_vehiculos:
            print(f"-{i.patente}")
        while True:
            auto_a_modificar = input("dime la patente del auto que deseas modificar: ")
            if i.patente == auto_a_modificar:
                nueva_velocidad = input(f"la velocidad actual de vehiculo es de {i.velocidad}, cual va a ser su nueva velocidad: ")
                self.velocidad = nueva_velocidad
                break
            else:
                print("esa patente no existe...")
    
    def tiempo_de_viaje(self):
        km = int(input("Ingrese los km a realizar: "))
        for i in self.lista_vehiculos:
            print(f"-{i.patente}")
        patente = input("dame la patente del auto que deseas modificar: ")
        while True:
            for i in self.lista_vehiculos:
                if i.patente == patente:
                    print(f" el auto tardara {km/i.velocidad} horas en realizar el viaje")
                else:
                    print("la patente no existe...")
            break
    
            

