categorias = ["Accion", "Deportivo", "Estrategia", "Simulacion"]

video_juegos=[['fifa'],['Deportivo'],[2021]]


def pedir_str(texto):
    while True:
        variable_str= input(texto)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()


def pedir_int(texto):
    while True:
        try:
            varaible_int = int(input(texto))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int


def imprimir_base(video_juegos):
    print('.......video juegos.......')
    print("JUEGO\t-\tCATEGORIA\t-\tAÑO")
    for i in range(len(video_juegos[0])): #cant filas
        print(f"{video_juegos[0][i]}\t-\t{video_juegos[1][i]}\t-\t{video_juegos[2][i]}")
    print(f"las categorias son: {categorias}")


def verificar_existencia (video_juegos):
    while True:
        juego = pedir_str("introduzca el nombre del juego: ")
        if juego in video_juegos[0]:
            print("este juego ya es existente!")
        else:
            return juego
        

def verificar_año (video_juegos):
    while True:
        año = pedir_int("deme el año del juego (este debe estar entre 1990 y 2021 ): ")
        if 2021>=año>=1990:
            return año
        else:
            print("este no es un año valido...")


def verificar_categoria(categorias):
    while True:
        categoria = pedir_str("introduzca su categoria: ")
        categoria = categoria.capitalize()
        if categoria in categorias:
            return categoria
        else:
            print("esta categoria no es existente!")
    

def agregar_juego(video_juegos):
    juego = verificar_existencia (video_juegos)
    año = verificar_año (video_juegos)
    categoria = verificar_categoria(categorias)
    video_juegos[0].append(juego)
    video_juegos[1].append(categoria)
    video_juegos[2].append(año)
    imprimir_base(video_juegos)
    print("se añadio exitosamente el nuevo juego!")
    return video_juegos


def eliminar_juego(video_juegos):
    while True:
        juego = pedir_str("nombre del juego a eliminar: ")
        if juego in video_juegos[0]:
            index = video_juegos[0].index(juego)
            video_juegos[0].pop(index)
            video_juegos[1].pop(index)
            video_juegos[2].pop(index)
            imprimir_base(video_juegos)
            print("juego eliminado exitosamente")
            return video_juegos
        else:
            print("este juego no existe!")


def editar_categoria(video_juegos):
    while True:
        juego = pedir_str("introduzca el nombre del juego: ")
        if juego in video_juegos[0]:
            pass
        else:
            print("este video juego no es existente!")
        categoria = pedir_str("introduzca su categoria: ")
        categoria = categoria.capitalize()
        if categoria in categorias:
            index = video_juegos[0].index(juego)
            video_juegos[1][index] = categoria
            imprimir_base(video_juegos)
            print("la categoria se cambio exitosamente!")
            return video_juegos
        else:
            print("esta categoria no es existente!")
    


def agregar_categorias():
    while True:
        categoria = pedir_str("que categoria desa agregar: ").capitalize
        if categoria in categorias:
            categorias.append(categoria)
            imprimir_base(video_juegos)
            print("se añadio exitosamente la categoria!")
            return video_juegos


def eliminar_categoria():
    while True:
        categoria = pedir_str("que categoria quieres eliminar: ").capitalize()
        if categoria in categorias:
            index = categorias.index(categoria)
            categoria.pop(index)
            return categoria
        else:
            print("esa categoria no existe...")


def main():
    imprimir_base(video_juegos)
    while True:
        menu = """--Programa de Agenda--
    1. Agregar un nuevo videojuego
    2. Eliminar un juego existente
    3. Ver lista de videojuegos
    4. Editar la categoria de un video juego
    5. Agregar categorias al sistema
    6. Eliminar una categoria del sistema
    7. Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
            agregar_juego(video_juegos)
        elif(opcion == "2"):
            eliminar_juego(video_juegos)
        elif(opcion == "3"):
            imprimir_base(video_juegos)
        elif(opcion == "4"):
            editar_categoria(video_juegos)
        elif(opcion == "5"):
            agregar_categorias()
        elif(opcion == "6"):
            eliminar_categoria()
        elif(opcion == "7"):
            return
        else:
            print('Opcion incorrecta')
