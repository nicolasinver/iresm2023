"""Contar con 6 funciones disponibles en el menu (estas funciones deben estar incluidas en una clase llamada GestorTaxis):

Crear instancias de choferes y guardarlos en una lista de choferes
Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
Modificar el chofer de un auto
Modificar el lugar de residencia del chofer indicando su nombre
imprmiir lista de choferes (con toda su informacion)
imprimir lista de autos (con toda su informacions)
Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes

Gestionar posibles errores

Estructurar el programa a criterio propio"""
from taxis import *

class GestorTaxis:
    def __init__ (self):
        self.lista_de_choferes : list[chofer] = []
        self.lista_de_taxis : list[autos] = []

    def crear_chofer(self):
        nombre = input("ingrese el nombre del chofer: ")
        apellido = input("ingrese su apellido: ")
        dni = input("ingrese su dni: ")
        fecha_nacimiento = input("ingrese su año de nacimiento: ") 
        Residencia = input("indique su residencia: ")
        chofer_nuevo = chofer(nombre, apellido, dni, fecha_nacimiento, Residencia)
        self.lista_de_choferes.append(chofer_nuevo)

    def crear_auto(self):
        choferes = []
        for chofer in self.lista_de_choferes:
            print(f"-{chofer.nombre}")
            choferes.append(chofer.nombre)
        if choferes:
            while True: 
                nombre_Chofer = input("Elija el chofer que será dueño del vehículo: ")
                for chofer in choferes:
                    if chofer == nombre_Chofer:
                        patente = input("ingrese su nueva patente: ") 
                        modelo = input("ingrese su modelo: ")
                        año = input("ingrese su año de ingreso a la empresa: ") 
                        marca = input("indique su marca: ")
                        auto_nuevo = autos(patente, modelo, año, marca, nombre_Chofer)
                        self.lista_de_taxis.append(auto_nuevo)
                        return
                print("Ese chofer no existe...")
        else:
            print("Todavía no hay ningún chofer existente...")

    def comprobar_chofer(self):
        if self.lista_de_choferes:
            for i in self.lista_de_choferes:
                print(f"-{i.nombre}")
            while True:
                nombre_chofer = input("elija a un chofer para modificar: ")
                for j in self.lista_de_choferes:
                    if j.nombre == nombre_chofer:
                        return nombre_chofer
                print("este chofer no existe...")
        else:
            print("todavia no hay choferes creados...")


    def modificar_chofer(self):
        if self.lista_de_taxis:
            for i in self.lista_de_taxis:
                print(f"-{i.patente}")
            while True:
                eleccion = input("ingrese la patente del auto a modificar: ")
                for j in self.lista_de_taxis:
                    if j.patente == eleccion:
                        nuevo_chofer = self.comprobar_chofer()
                        j.nombre_Chofer = nuevo_chofer
                        print(f"Chofer modificado para el auto con patente {eleccion}.")
                        return
        else:
            print("todavia no hay taxis disponibles...")
    
    
    def modificar_residencia(self):
        chofer_a_modificar = self.comprobar_chofer()
        for j in self.lista_de_choferes:
            nueva_residencia = input("indique su nueva residencia: ")
            j.Residencia == nueva_residencia
            print(f"la residencia de {chofer_a_modificar} se cambio exitosamente...")
            return
        

    def imprimir_info_taxis(self):
        print("--------- datos taxis ---------")
        for i in self.lista_de_taxis:
            print(F"patente: {i.patente}, modelo: {i.modelo}, año: {i.año}, marca: {i.marca}, chofer responsable: {i.nombre_Chofer}")
    
    def imprimir_info_choferes(self):
        print("--------- datos choferes ---------")
        for i in self.lista_de_choferes:
            print(F"nombre completo: {i.nombre} {i.apellido}, dni: {i.dni}, nacimiento: {i.fecha_nacimiento}, residencia: {i.Residencia}")

                    



