numero = int(input("ingresa un numero positivo para una cuenta regresiva: "))
for i in range(numero,0,-1):
    print(i, end=",")
    if i == 1:
        print("0")