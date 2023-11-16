"""Se debe crear una clase GestorHabitaciones que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de una habitacion y guárdalos en una lista de habitaciones. 
        1.1) Se debe verificar que tipo de instancia de Habitacion a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - numero: debe ser único
             - max_personas: verificar que sea un numero entero y este entre 2 y 6 inclusives.
             - precio: se debe pedir en pesos pero se debe guardar en dolares (1 dolar -> 900 pesos)
        1.2) Clases hijas:
             - cant_televisores: verificar que sea entero entre 0 y 3 incluses
             - Jacuzzi: verificar que sea True o False (boolean)
             
        1.3) Al crear una Habitacion es necesario logearlo (Escribir en una línea nueva: numero,max_personas,precio,tipo_de_clase)) 
             en un archivo llamado historial_habitaciones.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos y extension
    2.   Cambiar precio de habitacion, seleccionando su numero: Se debe cambiar el precio de la habitacion dependiendo de la cant max de 
         personas que contenga y el tipo de habitacion:
         - Se debe leer el diccionario por el tipo de habitacion y multiplicar ese precio por la cantidad de personas.
         Ej. Precio hab clasica = 400 (CL)* max_personas = 400 * 5 = 2000 IMPORANTE! solo se le pide el numero de habitacion al usuario
    3.   Pedir al usuario un numero y listar esa cantidad de habitaciones de la lista, verificando que hayan esa cantidad de habitaciones
    
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio"""
from hotel import *
class GestorHabitacion:
    def __init__(self):
        self.lista_habitaciones : list[Habitacion] = []

    def verificar_numero(self):
        while True:
            numero = int(input("Ingrese el numero de la habitacion: "))
            if numero not in self.lista_habitaciones:
                return numero
            else:
                print("El numero de la habitacion ya existe!")
                
    def verificar_max_personas(self):
        print("el numero de personas debe ser entre 2 y 6")
        while True:
            num_personas = input("ingrese el numero de personas para la habitacion: ")
            if 7> num_personas > 2:
                return num_personas
            else:
                print("numero de personas invalido...")

    def verificar_precio(self):
        while True:
            pedir_precio = input("dame el precio de la habitacion: ")
            if pedir_precio.isalnum():
                precio = (pedir_precio/900)
                return precio
            else:
                print("el precio no es un numero valido...")

    def elegir_tipo(self):
        lista_tipos = []
        for i in Habitacion.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        while True:
            tipo = input("elija el tipo de habitacion que desea crear: ")
            if tipo in lista_tipos:
                return str(tipo)
            else:
                print("este tipo de habitacion no es valido...")

    def comprobar_tv(self):
        while True:
            num_tv = input("dame un numero de televisiones entre 0 y 3")
            if 4>num_tv>-1:
                return num_tv
            else:
                print("numero de televisiones invalido...")
    
    def comprobar_jacuzzi(self):
        while True:
            respuesta = input("la habitacion tendra jacuzzi? (si o no): ").upper
            if respuesta == "SI":
                return True
            elif respuesta == "NO":
                return False
            else:
                print("respuesta invalida...")

    def crear_habitacion(self):
        numero = self.verificar_numero()
        personas = self.verificar_max_personas()
        precio = self.verificar_precio()
        tipo = self.elegir_tipo()
        if tipo == "comun":
            habitacion = comun(numero, personas, precio)
            self.lista_habitaciones.append(habitacion)
        elif tipo == "Clasica":
            num_tv = self.comprobar_tv()
            habitacion = Clasica(numero, personas, precio, num_tv)
            self.lista_habitaciones.append(habitacion)
        elif tipo == "Premium":
            jacuzzi = self.comprobar_jacuzzi()
            habitacion = Premium(numero, personas, precio, jacuzzi)
            self.lista_habitaciones.append(habitacion)
        texto = f'{numero},{personas},{precio},{tipo}'
        self.loguear(texto)


        
    def loguear(self,texto):
        try:
            fichero = open('log.csv','a+')
            fichero.write(texto+'\n')
            fichero.close()
        except Exception as e:
            print(e)

    def cambiar_precio(self):
        precio_habitaciones = {
        "Habitacion": 300, 
        "Clasica": 400,
        "Premium": 500
        }
        while True:
            numero_habitacion = input('ingrese el num de habitacion: ')
            for hab in self.lista_habitaciones:
                if hab.numero == numero_habitacion:
                    nuevo_precio = precio_habitaciones.get(hab.tipo_habitacion()) * hab.get_max_personas()
                    hab.setear_precio(nuevo_precio)
                    print(nuevo_precio)
                    return
            print('No existe esa habitacion')

    def verificar_numero(self):
        while True:
            nuevo_numero= input("dame el numero de la habitacion: ")
            for i in self.lista_habitaciones:
                if i.numero == nuevo_numero:
                    print("este numero ya es existente...")
                else:
                    return nuevo_numero
    
    def imprimir_info_completa(self):
        for i in self.lista_habitaciones:
            print(f"Habitacion numero: {i.numero} Maximo de Personas: {i.maxPersonas} Precio: {i.precio}")
                
    def listar_habitaciones(self):
        if self.lista_habitaciones:
            cont = 0
            num_a_ver = input("dame el numero de habitaciones a ver: ")
            for i in self.lista_habitaciones:
                print(f"Habitacion numero: {i.numero} Maximo de Personas: {i.maxPersonas} Precio: {i.precio}")
                cont+=1
                if cont == num_a_ver:
                    return

