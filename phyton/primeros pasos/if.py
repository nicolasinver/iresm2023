try:
    numero1 = int(input("ingresar un numero positivo: "))
    if(numero1<0):
        print(f"el numero {numero1} es negativo, no es lo que se pidio")
    if(numero1>0):
        print(f"el numero {numero1} es entero y positivo")
except Exception as e:
    print(f"el numero no es entero: {e}")
