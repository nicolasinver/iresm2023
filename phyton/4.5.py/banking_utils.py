saldo = 50000
def consult_balance():
    global saldo #
    pass

def insert_money():
    global saldo
    while True:
        try:
            monto_a_ingresar = float(input('Ingrese la cant de dinero: '))
            if monto_a_ingresar > 0 and monto_a_ingresar <1000000:
                saldo += monto_a_ingresar
                print(f'Nuevo monto = {saldo}')
                salir = input('Desea terminar la operacion? SI/NO: ')
                if salir.lower() == 'si':
                    break
                else:
                    continue
            else:
                print('El monto ingresado es incorrecto, ingrese nuevamente!')
        except Exception as e:
            print('Debe ingresar un numero!')

def extract_money():
    pass