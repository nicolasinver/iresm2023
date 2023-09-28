
base_frutas = [['fruta'],['stock']] 

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


def imprimir_base(base_frutas):
    print('-----base de frutas------')
    for i in range(len(base_frutas[0])): #cant filas
        print(f"{base_frutas[0][i]} \t {base_frutas[1][i]}")


def imprimir_base(base_verduras):
    print('-----base de verduras------')
    for i in range(len(base_verduras[0])): #cant filas
        print(f"{base_verduras[0][i]} \t {base_verduras[1][i]} \t ")

def agregar_stock_frutas(base_frutas):
    imprimir_base(base_frutas)
    nueva_fruta = pedir_un_str('Ingrese una nueva fruta: ')
    stock_de_la_fruta = pedir_un_int('Ingrese el stock fruta: ')
    base_frutas[0].append(nueva_fruta)
    base_frutas[1].append(stock_de_la_fruta)
    imprimir_base(base_frutas)

    return base_frutas

def consultar_stock(base_frutas):
    fruta_a_consultar =  pedir_un_str('Ingrese una fruta a consultar su stock: ')
    if(fruta_a_consultar in base_frutas[0]):
        index = base_frutas[0].index(fruta_a_consultar)
        print(f"El stock de {fruta_a_consultar} es: {base_frutas[1][index]}")
    else:
        print(f'La fruta {fruta_a_consultar} no pertenece al stock')


def eliminar_stock(base_frutas):
    fruta_a_eliminar =  pedir_un_str('Ingrese una fruta a eliminar: ')
    if(fruta_a_eliminar in base_frutas[0]):
        index = base_frutas[0].index(fruta_a_eliminar)
        base_frutas[0].pop(index)
        base_frutas[1].pop(index)
        print(f"Se elimino la fruta {fruta_a_eliminar}")      
    else:
        print(f'La fruta {fruta_a_eliminar} no pertenece al stock')

    return base_frutas
        
def eliminar_cant_del_stock(base_frutas):
    fruta_a_eliminar =  pedir_un_str('Ingrese una fruta a eliminar: ')
    if(fruta_a_eliminar in base_frutas[0]):
        cant_stock = pedir_un_int('Cant de stock a eliminar: ')
        index = base_frutas[0].index(fruta_a_eliminar)
        if(base_frutas[1][index]>=cant_stock):
            base_frutas[1][index] -= cant_stock
            imprimir_base(base_frutas)
            print("se elimino el stock exitosamente!")

        else:
            print('el stock no es suficiente')
    else:
        print(f'La fruta {fruta_a_eliminar} no pertenece al stock')
    
    return base_frutas

def menu():
    while True:
        menu = """
1. Agregar frutas
2. Consultar el stock de frutas
3. Eliminar un elemento del stock
4. Eliminar una cantidad de stock de alguna fruta
5. Listar tabla
6. Salir

opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                agregar_stock_frutas(base_frutas)
            case '2':
                consultar_stock(base_frutas)
            case '3':
                eliminar_stock(base_frutas)
            case '4':
                eliminar_cant_del_stock(base_frutas)
            case '5':
                imprimir_base(base_frutas)
            case '6':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')
        