"""El programa debe:

Contar con 4 funciones (suma, resta, división y multiplicación)
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los dos numero para operar y devolver el resultado al usuario
Gestionar posibles errores"""
def suma(a,b):
    try:
        suma =int(a)+int(b)
        print(f"la suma de {a} y {b} es: {suma}")
    except Exception as e:
        print(e)
def resta(a,b):
    try:
        suma =int(a)-int(b)
        print(f"la resta de {a} y {b} es: {suma}")
    except Exception as e:
        print(e)
def multiplicacion(a,b):
    try:
        suma =int(a)*int(b)
        print(f"la multiplicacion de {a} y {b} es: {suma}")
    except Exception as e:
        print(e)
def division(a,b):
    try:
        suma =int(a)/int(b)
        print(f"la division de {a} y {b} es: {suma}")
    except Exception as e:
        print(e)
while True:
    print ("suma(1), resta(2), multiplicacion(3), division(4)")
    eleccion = int(input("ingrese la opera que desea realizar: "))
    if 5>eleccion>0:
            break
    else:
        print("opcion invalida, vuelva a elegir")

a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))
if eleccion == 1:
    print(suma(a,b))
if eleccion == 2:
    print(resta(a,b))
if eleccion == 3:
    print(multiplicacion(a,b))
if eleccion == 4:
    print(division(a,b))


