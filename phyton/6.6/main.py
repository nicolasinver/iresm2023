from gestor import GestorTaxis
def menu():
    obj_gestor = GestorTaxis()
    while True:
        menu = """
1 - Crear chofer
2 - crear taxi
3 - modificar chofer
4 - imprimir lista de taxis
5 - imprimir lista de choferes
6 - cambiar residencia de un chofer
7 - salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_chofer()
            case '2':
                obj_gestor.crear_auto()
            case '3':
                obj_gestor.modificar_chofer()
            case '4':
                obj_gestor.imprimir_info_taxis()
            case '5':
                obj_gestor.imprimir_info_choferes()
            case '6':
                obj_gestor.modificar_residencia()
            case "7":
                return
            case _:
                print('opcion incorrecta')

if __name__ == "__main__":
    menu()