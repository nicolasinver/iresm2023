base_taxis = [["IRM-200","ABC-123","LOI-555"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

def pedir_un_str(texto_para_pedir):
    while True:
        variable_str = input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()


def cambiar_recorrido_auto(base_taxis):
    while True:
        patente = input('Dame la patente del auto a cambiar el chofer: ').upper()
        if patente in base_taxis[0]:
            nuevo_recorrido = pedir_un_int('Dame el nuevo recorrido: ')
            index = base_taxis[0].index(patente)
            base_taxis[2][index] = nuevo_recorrido
            print("recorrido cambiado correctamente!")
            return base_taxis
        else:
            print('No existe esa patente!')

def cambiar_chofer_auto(base_taxis):
    while True:
        patente = input('Dame la patente del auto a cambiar el chofer: ').upper()
        if patente in base_taxis[0]:
            nuevo_nombre = pedir_un_str('Dame el nombre del nuevo chofer: ')
            index = base_taxis[0].index(patente)
            base_taxis[1][index] = nuevo_nombre
            print("nombre cambiado correctamente!")
            imprimir_base(base_taxis)
            return base_taxis
        else:
            print('No existe esa patente!')

def imprimir_recorrdidos(base_taxis):
    recorrido = pedir_un_int('Ingrese el recorrido del viaje: ')
    print('Posibles choferes')
    for i in range(len(base_taxis[2])):
        if recorrido <= base_taxis[2][i]:
            print(f'auto: {base_taxis[0][i]} - chofer: {base_taxis[1][i]}')

def imprimir_base(base_taxis):
    print('-----base de taxis------')
    print("AUTO\t-\tCHOFER\t-\tRECORRIDO")
    for i in range(len(base_taxis[0])): #cant filas
        print(f"{base_taxis[0][i]}\t-\t{base_taxis[1][i]}\t-\t{base_taxis[2][i]}km")

def consultar_taxis(base_taxis):
    taxi_a_consultar =  input('Ingrese la patente del taxi a consultar: ').upper()
    if(taxi_a_consultar in base_taxis[0]):
        index = base_taxis[0].index(taxi_a_consultar)
        print("AUTO\t-\tCHOFER\t-\tRECORRIDO")
        print(f"{base_taxis[0][index]}\t-\t{base_taxis[1][index]}\t-\t{base_taxis[2][index]}km")
    else:
        print(f'La patente {taxi_a_consultar} no existe')

def pedir_patente(base_taxis):
    while True:
        letras = pedir_un_str("ingrese las tres letras de la patente: ").upper()
        if len(letras) == 3:
            numeros = str(pedir_un_int("ingrese ahora sus tres numeros: "))
            if len(numeros) == 3:
                patente = (f"{letras}-{numeros}")
                if patente in base_taxis[0]:
                    print("este vehiculo ya esta resgistrado")
                else:
                    base_taxis[0].append(patente)
                    break
            else:
                print("numeros invalidos...")
        else:
            print("letras invalidas...")

def agregar_taxi(base_taxis):
    pedir_patente(base_taxis)
    nombre = pedir_un_str("ingrese el nombre del chofer: ")
    base_taxis[1].append(nombre)
    recorrido = pedir_un_int("ingrese el recorrido del chofer: ")
    base_taxis[2].append(recorrido)
    imprimir_base(base_taxis)
    print("chofer agregado correctamente! ")
    return base_taxis

def eliminar_chofer(base_taxis):
   while True:
        patente = input('Dame la patente del auto a eliminar: ').upper()
        if patente in base_taxis[0]:
            index = base_taxis[0].index(patente)
            base_taxis[0].pop(index)
            base_taxis[1].pop(index)
            base_taxis[2].pop(index)
            imprimir_base(base_taxis)
            print("chofer eliminado correctamente!")
            return base_taxis
        else:
            print('No existe esa patente!')

def menu():
    imprimir_base(base_taxis)
    while True:
        menu = """
1. ver lista de taxis
2. Consultar algun taxi en especifico
3. cambiar un chofer
4. cambiar recorrido de un chofer
5. agregar chofer
6. eliminar chofer
7. realizar un viaje
8. Salir

opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                imprimir_base(base_taxis)
            case '2':
                consultar_taxis(base_taxis)
            case '3':
                cambiar_chofer_auto(base_taxis)
            case '4':
                cambiar_recorrido_auto(base_taxis)
            case '5':
                agregar_taxi(base_taxis)
            case '6':
                eliminar_chofer(base_taxis)
            case '7':
                imprimir_recorrdidos(base_taxis)
            case '8':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')
        

        

