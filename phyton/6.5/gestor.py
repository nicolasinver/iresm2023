
from computadora import Computadoras
"""Crear clase GestorComputadora que cuente con las siguientes funciones para un menu

Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
Listar Computadoras (presentandolos), indicando tipo.
Cambiar SO de una Computadora, verificando una lista de SO disponibles
Listar perifericos"""

class GestorComputadora:
    lista_marcas = ['dell','hp','apple']
    lista_SO = ['macOS','linux','windows']
    def __init__(self):
        self.lista_computadoras : list[Computadoras] = []

    def tipo_computadora(self):
        while True:
            print('------ Posibles pcs a crear ------')
            lista_tipos = []
            for i in Computadoras.__subclasses__():
                print(f"-{i.__name__}")
                lista_tipos.append(i.__name__)
            tipo = input("dame el tipo de computadora a crear: ")
            if tipo in lista_tipos:
                return tipo
            else:
                print("este tipo no existe... ")


    def pedir_so(self):
        while True:
            for i in self.lista_SO:
                print(f"-{i}")
            so = input("dame el so de la computadora: ")
            if so in self.lista_SO:
                return so
            else:
                print("ese so no existe...")
    
    def pedir_lista_perifericos(self):
        lista_perifericos = []
        while True:
            periferico = input(f'indique un perisferico (exit para terminar): ')
            if periferico == 'exit':
                return lista_perifericos
            else:
                lista_perifericos.append(periferico)



    def pedir_marca(self):
        while True:
            for i in self.lista_marcas:
                print(f"-{i}")
            marca = input("dame la marca de la computadora: ")
            if marca in self.lista_marcas:
                return marca
            else:
                print("ese so no existe...")

    def crear_computador(self):
        tipo_computadora_nueva = self.tipo_computadora()
        id = input("ingrese su nuevo id: ")
        so = self.pedir_so()
        marca = self.pedir_marca()
        if tipo_computadora_nueva == "notebook":
            peso = input("ingrese el peso del dispositivo: ")
            nueva_computadora = (id,so,marca,peso)
        elif tipo_computadora_nueva == "escritorio":
            memoria = input("ingrese la memoria del dispositivo: ")
            nueva_computadora = (id,so,marca,memoria)
        self.lista_computadoras.append(nueva_computadora)

    def listar_computadoras(self):
        for i in self.lista_computadoras:
            i.tipo_computadoras()
    
    def cambiar_so(self):
        while True:
            for i in self.lista_computadoras:
                print(f"- {i.id_modelo}")
            compu_a_modificar = input(f"dame la id de la computadora a modificar: ")
            for j in self.lista_computadoras:
                if compu_a_modificar == j.id_modelo:
                    nuevo_so = self.pedir_so()
                    self.SO = nuevo_so
                else:
                    print("esa id no existe...")
            break

    def listar_perifericos(self):
        id = input('Indique el id de la pc a listar los perifericos: ')
        for pcs in self.lista_computadoras:
            if pcs.id_modelo == id:
                pcs.listar_perifericos()
        







