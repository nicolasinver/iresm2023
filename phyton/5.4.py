"""# **Ejercicio 5.4**
Crear funciones que deban:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores"""

def pedir_un_str(texto_para_pedir):
    while True:
        try:
            varaible_str = input(texto_para_pedir)
            if varaible_str.isalpha():
                break
            else:
                print('Debe ingresar un valor tipo string!')
        except Exception as e:
            print('Debe ingresar un valor tipo string!')
    return varaible_str

def main():
    lista = []
    print("ingresa 5 materias")
    for i in range(0,5):
        materias = pedir_un_str(f"materia {i+1}: ")
        lista.append(materias)
    lista.sort()
    print(f'La lista en orden alfabetico es: {lista}')

if __name__ == "__main__":
    main()
