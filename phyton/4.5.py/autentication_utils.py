user = 'user'
contra = '1234'

def user_autentication():
    for i in range(3):
        usuario = input('Ingrese el usuario: ')
        constrasena = input('Ingrese la contraseña: ')
        if usuario == user and constrasena == contra:
            print('Usuario y contraseña correctos!')
            return True
        else:
            print(f'Usuario y contraseña incorrectos, le quedan {2-i} intentanos')
    # si salgo del for es porque agote mis 3 intentos
    return False