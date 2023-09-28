from banking_utils import *

def menu():
    while True:
        menu = """
Mediciones 
1.   Consultar el saldo
2.   Ingresar dinero
3.   Retirar dinero
4.   Salir

opcion: """
    
        opcion = input(menu)
        match opcion:
            case '1':
                pass
            case '2':
                insert_money()
            case '3':
                pass
            case '4':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')

def menu_2():
    while True:
        menu = """
Mediciones 
1.   Consultar el saldo
2.   Ingresar dinero
3.   Retirar dinero
4.   Salir

opcion: """
    
        opcion = input(menu)
        if(opcion == '1'):
            pass
        elif(opcion == '2'):
            pass
        elif(opcion == '3'):
            pass
        elif(opcion == '4'):
            print('Saliendo')
            return
        else:
            print('opcion incorrecta')


def get_pass():
    import getpass

    try:
        p = getpass.getpass()
    except Exception as err:
        print('ERROR:', err)
