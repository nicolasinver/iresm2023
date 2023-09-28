import math 
def area_cuadrado (a,b):
    try:
        area =float(a)*float(b)
        print(f"el area de un cuadrado de {a} por {b} es: {area}")
    except Exception as e:
        print("mal argumento")
def area_circulo (a):
    try:
        area =(float(a)**2)*math.pi
        print(f"el area de un circulo de {a} de radio  es: {area}")
    except Exception as e:
        print("mal argumento")
def perimetro_cuadrado (a,b):
    try:
        perimetro = (float(a)+float(b))*2
        print(f"el area de un circulo de {a} de radio  es: {perimetro}")
    except Exception as e:
        print("mal argumento")
def perimetro_circulo (a):
    try:
        perimetro = math.pi* 2 * float(a)
        print(f"el area de un circulo de {a} de radio  es: {perimetro}")
    except Exception as e:
        print("mal argumento")

def pedir_dos_argumentos_float(texto_1,texto_2):
    while True:
        try:
            num_1 = float(input(texto_1))
            num_2 = float(input(texto_2))
            return num_1,num_2
        except Exception as e:
            print('Los argumentos deben ser decimales o enteros')
def pedir_un_argumentos_float(texto_1):
    while True:
        try:
            num_1 = float(input(texto_1))
            return num_1
        except Exception as e:
            print('Los argumentos deben ser decimales o enteros')

def menu():
    while True:
        menu = """
        CALCULADORA DE AREAS Y PERIMETROS
        1.   area de un cuadrado
        2.   area de un circulo
        3.   perimetro de un cuadrado
        4.   perimetro de un circulo
        5.   Salir

        opcion: """
    
        opcion = input(menu)
        if opcion in ['1','3']:
            a,b = pedir_dos_argumentos_float('Dame el primer lado:','Dame el segundo lado: ')
        elif opcion in ['2','4']:
            a = pedir_un_argumentos_float('Dame su radio: ')
        match opcion:
            case '1':
                area_cuadrado (a,b)
            case '2':
                area_circulo (a)
            case '3':
                perimetro_cuadrado (a,b)
            case '4':
                perimetro_circulo (a)
            case '5':
                print('Saliendo')
                break
            case _:
                print('opcion incorrecta')
menu()


