import os
import PyPDF2

from vvalley import extract_vvalley_data, crear_nombre_factura_vvalley
from ingram import extract_ingram_data, crear_nombre_factura_ingram
#from infratech import extract_infratech_data, crear_nombre_factura_infratech

from files import crear_carpeta, copiar_y_renombrar_pdf

proveedores = ['V-Valley', 'TeamViewer', 'Repsol', 'INGRAM', 'Infratech']
ruta_carpeta = './facturas'

def buscar_palabras_en_pdf(ruta_carpeta, proveedores):
    procesados = []
    # Recorrer todos los archivos en la carpeta
    for nombre_archivo in os.listdir(ruta_carpeta):
        # Verificar que el archivo sea un PDF
        if nombre_archivo.endswith('.pdf') or nombre_archivo.endswith('.PDF'):
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            # Leer el contenido del PDF
            with open(ruta_archivo, 'rb') as archivo_pdf:
                lector_pdf = PyPDF2.PdfReader(archivo_pdf)
                texto_completo = ""
                # Extraer el texto de cada página del PDF
                for num_pagina in range(len(lector_pdf.pages)):
                    pagina = lector_pdf.pages[num_pagina]
                    texto_completo += pagina.extract_text()
                # Buscar las palabras en el texto completo
                for palabra in proveedores:
                    if palabra in texto_completo:
                        print(f'La palabra "{palabra}" fue encontrada en el archivo "{nombre_archivo}".')
                        procesados.append(archivo_pdf)
                        if palabra == 'V-Valley':
                            data = extract_vvalley_data(texto_completo)
                            nombre_nuevo_archivo = crear_nombre_factura_vvalley(data)
                            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/Pend_Archivar', nombre_nuevo_archivo)
                        if palabra == 'INGRAM':
                            data = extract_ingram_data(texto_completo)
                            nombre_nuevo_archivo = crear_nombre_factura_ingram(data)
                            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/Pend_Archivar', nombre_nuevo_archivo)
                        if palabra == 'Repsol':
                            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/Pend_Archivar', nombre_archivo)
                   
    for nombre_archivo in os.listdir(ruta_carpeta):
                # Verificar que el archivo sea un PDF
        if nombre_archivo not in procesados:
            copiar_y_renombrar_pdf(ruta_archivo, nombre_archivo, ruta_archivo + '/sin_clasificar', nombre_archivo)
                        


crear_carpeta(ruta_carpeta + '/Pend_Archivar')
crear_carpeta(ruta_carpeta + '/sin_clasificar')

buscar_palabras_en_pdf(ruta_carpeta, proveedores)
