import os
import shutil

# Ruta de la carpeta a organizar
carpeta = r'C:\Users\$$$\Downloads'

# Mapeo de extensiones de archivo a carpetas
clasificacion_archivos = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Música': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Archivos Comprimidos': ['.zip', '.rar', '.7z'],
}

# Crear las carpetas si no existen
for carpeta_destino in clasificacion_archivos:
    ruta_carpeta = os.path.join(carpeta, carpeta_destino)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Organizar los archivos
for archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, archivo)

    # Ignora si es una carpeta
    if os.path.isdir(ruta_archivo):
        continue

    # Mueve el archivo a la carpeta correspondiente según su extensión
    _, extension = os.path.splitext(archivo)
    for carpeta_destino, extensiones in clasificacion_archivos.items():
        if extension.lower() in extensiones:
            shutil.move(ruta_archivo, os.path.join(carpeta, carpeta_destino, archivo))
            print(f'Moviendo {archivo} a {carpeta_destino}')
            break