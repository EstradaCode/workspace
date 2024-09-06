##archivo = open ('archivo.txt',"w")
#archivo.write("hola como estas??\n todo bien ???")
#ciudades= ["formosa\n", "buenos aires\n", "rio negro\n"]
#with open('archivo.txt', 'r') as archivo:
#    lineas = archivo.readlines()
#    for linea in lineas:
#        print(linea.strip())

try:
    with open ('archivo.txt', 'r+') as archivo:
        archivo.truncate(10)
except FileNotFoundError:
    print("el archivo no se encontró.")
except IOError as e:
    print(f"Error de i/o: {e}")

import os as so
archivos = so.listdir('.')
print(archivos)