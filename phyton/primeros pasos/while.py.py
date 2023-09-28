flag = True
try:
    while flag:
        dato_1 = (input("ingresa un numero entero: "))
        dato_2 = (input("ingresa un segundo numero: "))
        dato_3 = (input("ingresa un tercer numero: "))
        dato_4 = (input("ingresa un cuarto numero: "))
        dato_5 = (input("ingresa un quinto numero: "))
        if (dato_1.isdigit() and dato_2.isdigit() and dato_3.isdigit() and dato_4.isdigit() and dato_5.isdigit()):
            dato_1 = int(dato_1)
            dato_2 = int(dato_2)
            dato_3 = int(dato_3)
            dato_4 = int(dato_4)
            dato_5 = int(dato_5)
            print (f"el promedio de estos numeros es: {(dato_1 + dato_2 + dato_3 + dato_4 + dato_5)/5}")
            flag = False
        else:
            print("los numeros ingresados no son enteros")
except Exception as e:
    print (f"el error es: {e}")