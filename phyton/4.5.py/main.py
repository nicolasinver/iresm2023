from utils import menu
from autentication_utils import user_autentication
#import utils

def main():
    if user_autentication():
        menu()
    else:
        print('Saliendo')
    #utils.menu()

# buena practica
if __name__ == "__main__":
    main()