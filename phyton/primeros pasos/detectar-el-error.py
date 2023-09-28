try:
    dato1 = int(input("dame un dato numerico: "))
    dato2 = int(input("dame un segundo dato numerico: "))
    dato3 = (dato1 + dato2)
    print(f"la suma de {dato1} y {dato2} es {dato3}")
except Exception as e:
    print(f"error: {e}")
