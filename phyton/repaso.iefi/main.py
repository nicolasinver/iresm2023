import os
#path actual
#path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
from gestor import *
def menu():
    obj_gestor = GestorHabitacion()
    while True:
        menu = """
    
        1 - Crear Habitacion
        2 - Cambiar precio
        3 - Listar habitaciones
        4 - Salir
        opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_habitacion()
            case '2':
                obj_gestor.cambiar_precio()
            case '3':
                obj_gestor.listar_habitaciones()
            case '4':
                return
            case _:
                print("opcion invalida...")

if __name__ == "__main__":
    menu()