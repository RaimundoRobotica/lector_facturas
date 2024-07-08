from read import buscar_palabras_en_pdf
from files import crear_carpeta

ruta_carpeta = './facturas'
proveedores = ['V-Valley', 'Repsol', 'INGRAM', 'Infratech']

if __name__ == '__main__':
    crear_carpeta(ruta_carpeta + '/Pend_Archivar')
    crear_carpeta(ruta_carpeta + '/sin_clasificar')
    buscar_palabras_en_pdf(ruta_carpeta, proveedores)
