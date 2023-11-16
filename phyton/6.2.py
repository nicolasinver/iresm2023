"""Crear una clase de FiguraGeometrica:

Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
Se deben crear 3 metodos en la clase:
Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
Cambiar color de figura e indicar nuevo color
verificar si la figura es tamaño pequeño, agrandar a tamaño grande"""

class FiguraGeometrica:
    def __init__(self,tipo_de_figura, color, tamaño = "pequeño"):
        self.tipo_de_figura = tipo_de_figura
        self.color = color
        self.tamaño = tamaño

    def cambiar_color(self,color):
        self.color = color

    def mostrar_info(self):
        print(f"soy un {self.tipo_de_figura} de color {self.color} y de tamaño {self.tamaño}")

    def verificar_tamaño(self):
        if self.tamaño == "pequeño":
            print("agrandando su tamaño...")
            self.tamaño = "grande"
        else:
            print("esta figura ya es grande")

figura_1 = FiguraGeometrica("circulo", "rojo")
figura_2 = FiguraGeometrica("cuadrado", "azul", "grande")
figura_1.mostrar_info()
figura_1.cambiar_color("azul")
figura_1.verificar_tamaño()
figura_1.mostrar_info()
figura_2.mostrar_info()
figura_2.cambiar_color("violeta")
figura_2.verificar_tamaño()
figura_2.mostrar_info()
