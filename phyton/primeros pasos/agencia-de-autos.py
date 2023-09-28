try:
    dinero = int(input("""los precios son:
    - bugatti = 50000
    - rollroyce: 105000
    - audi = 190000
    ahora ingrese la cantidad de dinero con la que cuenta: """))
    bugatti = 50000
    rollroyce = 105000
    audi = 190000
except Exception as e:
    print(f"el numero no es entero: {e}")
if dinero>=audi:
 print("usted puede comprar un audi, un rollroyce o un bugatti")
else:
 if audi>dinero>=rollroyce:
  print("usted puede comprar un rollroyce o bugatti")
 else:
  if rollroyce>dinero>=bugatti:
   print("usted solo puede comprar un bugatti")
  else:
   print("usted no puede comprar ningun vehiculo")
