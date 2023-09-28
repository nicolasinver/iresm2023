flag = True
while flag:
     try:
      palabra = input("escribe una palabra: ")
      if (palabra.isalpha()): 
       flag=False
      else:
       print("la palabra no contiene solo letras del alfabeto")
     except Exception as e:
         print ("el dato ingresado debe ser una letra")  

flag2 = True
while  flag2:
     try:
      numero = input("ingrese el numero de veces que desea repetir la palabra: ")
      if (numero.isdigit()):
       numero = int(numero)
       flag2=False
      else:
       print("el numero no es un entero")
     except Exception as e:
         print ("el dato ingresado debe ser un entero")  
cont = numero
for _ in range(numero):
 print (palabra)

       
    
