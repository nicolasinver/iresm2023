try: 
    dinero_acumulado = 0
    dinero = float(input("ingresa una cantidad de dinero a invertir: "))
    interes = float(input("ingresa el porcentaje de interes anual: "))
    años = int(input("ingresa la cantidad de años que quiere llevar a cabo la inversion: "))
    dinero_acumulado = 0
    for anio in range (0,años,1):
        dinero_acumulado = dinero + dinero*interes
        dinero = dinero_acumulado
        print (f"el interes compuesto ={dinero_acumulado}")
except Exception as e:
    print(e)