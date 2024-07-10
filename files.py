import os
import shutil

def crear_carpeta(ruta_carpeta):
    # Comprobar si la carpeta existe
    if not os.path.exists(ruta_carpeta):
        # Si no existe, crear la carpeta
        os.makedirs(ruta_carpeta)
        print(f"Carpeta creada: {ruta_carpeta}")
    else:
        print(f"La carpeta ya existe: {ruta_carpeta}")


def copiar_y_renombrar_pdf(ruta_origen, nombre_archivo, ruta_destino, nuevo_nombre):
    # Ruta completa del archivo de origen
    archivo_origen = os.path.join(ruta_origen, nombre_archivo)
    # Ruta completa del archivo de destino con el nuevo nombre
    archivo_destino = os.path.join(ruta_destino, nuevo_nombre)
    
    # Verificar si el archivo de origen existe
    if os.path.exists(archivo_origen):
        # Copiar y renombrar el archivo
        shutil.copy2(archivo_origen, archivo_destino)
        print(f"Archivo copiado y renombrado a: {archivo_destino}")
    else:
        print(f"El archivo de origen no existe: {archivo_origen}")

def pregunta_direccion():
    print('Escribe la dirección donde se encuentran tur facturas.')
    print('Enter si el ejecutable ya está en la carpeta.')
    direccion = input('> ')
    if direccion == '':
        return './'
    else:
        return direccion