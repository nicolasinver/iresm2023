
while True:
    try:
        cantidad_personas = int(input("Ingrese la cantidad de personas: "))
        break
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        exit()

edad_mayor = 0

for i in range(cantidad_personas):
    try:
        edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    except ValueError:
        print(f"Error: Debe ingresar una edad válida para la persona {i}.")
        exit()
    if edad > edad_mayor:
        edad_mayor = edad
print(f"la edad mayor es de {edad_mayor} años")