"""El programa debe:

Contar con 3 funciones:
Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o frase (Ambos parametros)
Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.IMPORANTE:deben ser palabras y no frases (verificar)
Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los parametros y devolver el resultado al usuario
Gestionar posibles errores"""


def contador_letras_sin_espacios(frase):
    contador = 0
    for caracter in frase:
        if caracter.isalpha():
            contador += 1
    return contador


def comparador_de_palabras(palabra1,palabra2):
    while(True):
        if not palabra1.isalpha() or not palabra2.isalpha():
            print ("Ambas entradas deben ser palabras")
        else:
            break
    if len(palabra1)>len(palabra2):
        print(f"la palabra 1 tiene {len(palabra1)} letras, esta es la palabra de mas letras")
    elif len(palabra1)<len(palabra2):
        print(f"la palabra 12 tiene {len(palabra2)} letras, esta es la palabra de mas letras")
    else:
        print(f"las dos palabras tienen la misma cantidad de letras, ambas tienen {len(palabra1)} letras")


def quitador_de_vocales(palabra):
    palabra_sin_vocales = ""
    for letra in palabra:
        if letra not in "aeiouAEIOU":
            palabra_sin_vocales += letra
    return palabra_sin_vocales


def pedir_palabras():
    while True:
        try:
            palabra1 = input("ingresa la primera palabra: ")
            palabra2 = input("ingresa la segunda palabra: ")
            if palabra1.isalpha() and palabra2.isalpha():
                return palabra1, palabra2
            else:
                print("debe ser una sola palabra y los argumentos deben ser letras del alfabeto")
        except Exception as e:
            print('Los argumentos deben ser letras del alfabeto')


def pedir_palabra():
    while True:
        try:
            palabra1 = input("ingresa una palabra: ")
            if palabra1.isalpha():
                return palabra1
            else:
                print("debe ser una sola palabra y los argumentos deben ser letras del alfabeto")
        except Exception as e:
            print(f'Los argumentos deben ser letras del alfabeto{e}')


def pedir_frase():
    while True:
        try:
            frase = input("ingresa una frase o palabra: ")
            return frase
        except Exception as e:
            print(f'Los argumentos deben ser letras del alfabeto{e}')


def main():
    while True:
        menu = """
        Calculadora de palabra
        1.   Contar las letras de una palabra o frase
        2.   Comparar que frase tiene mas letras
        3.   Quitar las vocales de una palabra
        4.   Salir

        opcion: """
    
        opcion = input(menu)
        match opcion:
            case '1':
                frase = pedir_frase()
                print(f"La frase o palabra tiene {contador_letras_sin_espacios(frase)} letras")
            case '2':
                palabra1, palabra2 = pedir_palabras()
                print (comparador_de_palabras(palabra1,palabra2))
            case '3':
                palabra = pedir_palabra()
                print (quitador_de_vocales(palabra))
            case '4':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')


main()
