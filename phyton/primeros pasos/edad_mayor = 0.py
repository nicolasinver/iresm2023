edad_mayor = 0
try: 
    while (True):
        edad_mayor = 0
        personas = int(input("dame un numero de personas: "))
        if personas>0:
            break
        else:
            print("no se ingreso un numero valido de personas")
    while (True):
        for edad in range (personas):
                i = 0
                edad = int(input(f"dame la edad de la persona {i+1}: "))
                if edad>=0:
                    continue
                else:
                    print("no se ingreso un numero valido de años")
                if edad > edad_mayor:
                    edad_mayor = edad
        print(f"la edad mayor es de {edad_mayor} años")
except Exception as e:
   print(e)