import os.path as path
# verifico que existe el archivo
nombre_archivo="dataa.csv"
if path.isfile(nombre_archivo):
# si es asi, abro el archivo y lo leo
    with open(f"./{nombre_archivo}", "r") as archivo:
        print(f"contenido del archivo {nombre_archivo}:")
        print(archivo.read())
    # todo dentro del with tiene su open y close, por lo que no hace falta colocarlo
else:
    print (f"el archivo {nombre_archivo} no existe")