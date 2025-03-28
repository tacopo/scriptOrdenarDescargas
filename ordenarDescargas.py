import os
import shutil

def ordenar_descargas(directorio_descargas):
    if not os.path.exists(directorio_descargas):
        print(f"El directorio {directorio_descargas} no existe.")
        return

    for archivo in os.listdir(directorio_descargas):
        ruta_archivo = os.path.join(directorio_descargas, archivo)

        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1][1:].lower()  # Obtener la extensión sin el punto
            if not extension:  # Si no tiene extensión, usar "sin_extension"
                extension = "sin_extension"

            carpeta_destino = os.path.join(directorio_descargas, extension)

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

if __name__ == "__main__":
    directorio_descargas = os.path.expanduser("~/Downloads")  # Cambiar si el directorio es diferente
    ordenar_descargas(directorio_descargas)