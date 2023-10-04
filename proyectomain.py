import modulomatriz
import modulomorse
import sys

def menuprincipal():
    preg = input("""Indique lo que desea hacer: 
    1 - Traductor de morse
    2 - Matriz
    3 - Salir
    """)
    if preg == '1':
        modulomorse.proyectoMorse()
    elif preg == '2':
        modulomatriz.proyectoMatriz()
    elif preg == '3':
        print("Hasta la próxima")
        sys.exit()
    else:
        print(f"La opción '{preg}' no existe, por favor indique una de las existentes")
        menuprincipal()

print(menuprincipal())
