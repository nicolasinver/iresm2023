productos = [["agua","soda","coca"],[300,400,500],[5,4,7]]

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


def imprimir_base(productos):
    print('-----productos------')
    for i in range(len(productos[0])): #cant filas
        print(f"{productos[0][i]} \t {productos[1][i]} \t {productos[2][i]}")


def pago_efectivo(producto):
    if producto in productos[0]:
        index = productos[0].index(producto)
        print(f"el valor del producto sera de {productos[1][index]*(0.90)}")
        productos[2][index] -= 1
    else:
        print("ese producto no es existente...")
    return productos


def pago_debito(producto):
    if producto in productos[0]:
        index = productos[0].index(producto)
        print(f"el valor del producto sera de {productos[1][index]}")
        productos[2][index] -= 1
    else:
        print("ese producto no es existente...")
    return productos


def pago_credito(producto):
    if producto in productos[0]:
        index = productos[0].index(producto)
        print(f"el valor del producto sera de {productos[1][index]*(1.1)}")
        productos[2][index] -= 1
    else:
        print("ese producto no es existente...")
    return productos


def consultar_stock(productos):
    producto_a_consultar =  pedir_un_str('Ingrese una fruta a consultar su stock: ')
    if(producto_a_consultar in productos[0]):
        index = productos[0].index(producto_a_consultar)
        print(f"El stock de {producto_a_consultar} es: {productos[1][index]}")
    else:
        print(f'La fruta {producto_a_consultar} no pertenece al stock')


def agregar_stock(productos):
    producto = pedir_un_str("de que producto quiere agregar stock: ")
    if producto in productos[0]:
        cantidad = pedir_un_int("cuanta cantidad de stock desea agregar: ")
        index = productos[0].index(producto)
        producto[2][index] += cantidad
    else:
        print("el producto no existe...")


def cambiar_precios(productos):
    producto = pedir_un_str("de que producto quiere cambiar su precio: ")
    if producto in productos[0]:
        precio = pedir_un_int("que precio quiere ponerle: ")
        index = productos[0].index(producto)
        producto[1][index] = precio
    else:
        print("el producto no existe...")


def elegir_medio_pago(productos):
    while True:
        opcion_1 = pedir_un_str('''
Eliga el medio de pago
- Efectivo (E) (-10 porciento)
- Tarjeta debito (TD) 
- Tarjeta credito (TC) (+10 porciento)
Opcion: ''')
        match opcion_1:
            case "e":
                pago_efectivo(productos)
                return productos
            case"td":
                pago_debito(productos)
                return productos
            case"tc":
                pago_credito(productos)
                return productos
            case _:
                print('opcion incorrecta')


def menu():
    while True:
        opcion = input('''
Eliga una opcion
  1. Ver menu de productos
  2. Comprar un producto
  3.  consultar productos y stock
  4.  agregar stock a los productos
  5.  cambiar el precio a los productos
  6.  Salir
Opcion: ''')
        
        match opcion:
            case "1":
                imprimir_base(productos)
            case "2":
                producto = pedir_un_str("que producto desea comprar: ")
                producto = elegir_medio_pago(producto)
            case "3":
                consultar_stock(productos)
            case "4":
                productos = agregar_stock(productos)
            case "5":
                productos = cambiar_precios(productos)
            case _:
                print('opcion incorrecta')