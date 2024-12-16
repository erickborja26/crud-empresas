import os
from time import sleep
from lib_empresas import *

### RUBRICA DE CALIFICACION
### MENU DE OPCIONES 2 PUNTOS
### REGISTRAR 5 PUNTOS
### MOSTRAR 3 PUNTOS
### ACTUALIZAR 5 PUNTOS
### ELIMINAR 3 PUNTOS
### GRABAR EN ARCHIVO DE TEXTO 4 PUNTOS
opcion= 0
cargar_empresas("empresas.txt")

while(opcion<5):
    os.system("clear")
    menu()
    opcion= int(input("INGRESE LA OPCION: "))
    os.system("clear")
    if opcion==1:
        registrar()
    elif opcion==2:
        mostrar()
    elif opcion==3:
        actualizar()
    elif opcion==4:
        eliminar()
    elif opcion==5:
        mostrar_mensaje("[5] SALIR")
        grabar_empresas("empresas.txt")
    else:
        mostrar_mensaje("OPCION INCORRECTA!!!")
    sleep(2)
    