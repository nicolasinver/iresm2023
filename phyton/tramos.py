"""Ejercicio 3.20
El programa debe:

Pedir al usuario una cantidad de tramos de un viaje
pedir al usuario la duracion en minutos de cada tramo
calcular el tiempo total de viaje
no deben generar errores"""
try: 
    tramos= int(input("cuentos tramos realizara en su viaje: "))
    cont = 0
    cont1 = 0   
    for i in range (tramos):
        cont1+=1
        min = int(input(f"ingrese la duracion del tramo (en minutos) {cont1}: "))
        cont+=min
    print (f"la cantidad de minutos en total son {cont} minutos")
except Exception as e:
    print(e)

