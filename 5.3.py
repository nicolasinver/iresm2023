def pedir_una_palabra():
    while True:
        palabra = input("dame una palabra o frase: ")
        palabra = palabra.replace(" ","")
        if palabra == palabra.isalpha():
            if palabra == palabra[::-1]:
                print("es un palindromo")
                break
            else:
                print("no es un palindromo")
                break
        else:
            print("no es una palabra o frase...")

pedir_una_palabra()