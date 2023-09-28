viaje = [[],[]]

def pedir_un_str(texto_para_pedir):
    while True:
        variable_str= input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

def imprimir_base(viajes):
    print('-----base de viajes------')
    for i in range(len(viajes[0])): #cant filas
        print(f"{i+1}- {viajes[0][i]} km \t {viajes[1][i]} m")


def agregar_tramos(viaje):
    tramo = pedir_un_int("cuantos km desea recorrer?: ")
    duracion = pedir_un_int("cuantos minutos dura recorrer el tramo?: ")
    viaje[0].append(tramo)
    viaje[1].append(duracion)

    return viaje

def borrar_tramos(viaje):
    tramo = pedir_un_int("que tramo desea eliminar?: ")
    if tramo in viaje[0]:
        index = viaje[0].index(tramo)
        viaje[0].pop(index)
        viaje[1].pop(index)
    else:
        print("el tramo no existe...")
    return viaje

def consultar_duracion(viaje):
    tramo = pedir_un_int("que tramo desea consultar?: ")
    if tramo in viaje[0]:
        index = viaje[0].index(tramo)
        print(f"el viaje tiene {viaje[0][index]} km y dura {viaje[1][index]} minutos")

def duracion_total(viaje):
    kilometros = sum(viaje[0])
    duracion = sum(viaje[1])
    print(f"los tramos tendran un total de {kilometros} km y durara {duracion} minutos")
        

def menu():
    while True:
        menu = """
1. Agregar mas tramos
2. borrar tramos
3. ver la duracion de un tramo
4. ver la duracion total de todos los tramos
5. Listar tabla
6. Salir

opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                agregar_tramos(viaje)
            case '2':
                borrar_tramos(viaje)
            case '3':
                consultar_duracion(viaje)
            case '4':
                duracion_total(viaje)
            case '5':
                imprimir_base(viaje)
            case '6':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')
        


    