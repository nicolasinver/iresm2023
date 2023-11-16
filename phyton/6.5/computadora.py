"""Crear una clase padre Computadoras:

Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO,marca)
Crear metodos para esta clase de:
Presentarse (id_modelo,listaPerifericos,SO)
Indicar tipo de Computadora (Clases heredadas)
Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO
Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una

Escritorio
Notebook
Crear clase GestorComputadora que cuente con las siguientes funciones para un menu

Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
Listar Computadoras (presentandolos), indicando tipo.
Cambiar SO de una Computadora, verificando una lista de SO disponibles
Listar perifericos"""

class Computadoras:
    def __init__(self,id_modelo,listaPerifericos: list,SO,marca):
        self.id_modelo = id_modelo
        self.listaPerifericos = listaPerifericos 
        self.SO = SO
        self.marca = marca
    
    def CambiarSO(self,so_nuevo):
        self.SO = so_nuevo

    def tipo_computadoras(self):
        print(f"Soy una compu del tipo {type(self).__name__}")
    
    def listar_perifericos(self):
        print("mis perifericos son: ")
        for per in self.listaPerifericos:
            print(f"-{per}")

    
    
class escritorio(Computadoras):
    def __init__(self,id_modelo,listaPerifericos,SO,marca,memoria):
        super().__init__(id_modelo,listaPerifericos,SO,marca)
        self.memoria = memoria

class notebook(Computadoras):
    def __init__(self,id_modelo,listaPerifericos,SO,marca, peso):
        super().__init__(id_modelo,listaPerifericos,SO,marca)
        self.peso = peso

