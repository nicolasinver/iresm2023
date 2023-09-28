contraseña = "gato123"
prueba_de_contraseña = input("introduce una contraseña:").lower()
try: 
    if (contraseña==prueba_de_contraseña):
     print("la contraseña es correcta")
    else: 
       print("la contraseña es incorrecta")
except Exception as e:
    print(f"el erro es: {e}")