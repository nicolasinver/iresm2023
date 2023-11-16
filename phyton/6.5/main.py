from gestor import GestorComputadora
def menu():
    # instancio un objeto de gestor de computadoras para usar sus metodos
    obj_gestor = GestorComputadora()
    while True:
        menu = """
1.   Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
2.   Listar Computadoras (presentandolos), indicando tipo.
3.   Cambiar SO de una Computadora, verificando una lista de SO disponibles
4.   Listar perifericos
5.   Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_computador()
            case '2':
                obj_gestor.listar_computadoras()
            case '3':
                obj_gestor.cambiar_so()
            case '4':
                obj_gestor.listar_perifericos()
            case '5':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()