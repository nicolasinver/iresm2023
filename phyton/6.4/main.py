from gestor import GestorAutos
def menu():
    obj_gestor = GestorAutos()
    while True:
        menu = """
1 - Crear auto, indicando tipo de auto y guardar en una lista
2 - Listar autos (presentandolos), indicando tipo de Vehiculo.
3 - Cambiar velocidad de un Vehiculo
4 - Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
5 - SALIR
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_auto()
            case '2':
                obj_gestor.presentaciones()
            case '3':
                obj_gestor.cambiar_velocidad()
            case '4':
                obj_gestor.tiempo_de_viaje()
            case '5':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()