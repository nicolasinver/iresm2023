flag = True
while flag:
        try:
         numero1 = int(input("ingresa un numero del 1 al 9: "))
         if (10> numero1 >=1):
            flag = False
         else: 
            print("el numero no esta dentro del rango determinado") 
        except Exception as e:
         print ("el dato ingresado debe ser entero")   
cont = 1
while cont <=10:
   print(f"{numero1}x{cont} = {numero1*cont}")
   cont+=1
   