from read import buscar_palabras_en_pdf
from files import crear_carpeta

# Ruta relativa donde se encuentran las facturas que hay que procesar
ruta_carpeta = './facturas'
# Proveedores actualmente soportados
proveedores = ['V-Valley', 'Repsol', 'INGRAM', 'Infratech']

if __name__ == '__main__':
    # Creación de carpetas de almacenamiento
    crear_carpeta(ruta_carpeta + '/Pend_Archivar')
    crear_carpeta(ruta_carpeta + '/sin_clasificar')
    # Lectura y escritura de los archivos que hay en la carpeta:
    buscar_palabras_en_pdf(ruta_carpeta, proveedores)
