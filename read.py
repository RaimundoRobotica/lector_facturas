import os
import PyPDF2

from vvalley import extract_vvalley_data, crear_nombre_factura_vvalley
from ingram import extract_ingram_data, crear_nombre_factura_ingram
#from infratech import extract_infratech_data, crear_nombre_factura_infratech
from files import copiar_y_renombrar_pdf


def buscar_palabras_en_pdf(ruta_carpeta, proveedores):
    '''
    ruta_carpeta (str): Ruta donde se encuentran las facturas sin procesar
    proveedores (list): Lista de proveedores actualmente soportados con funciones propias de extracción
    
    Para que la función pueda trabajar, aparte de archivos en PDF, tiene que haber dos carpetas para ordenar
    los archivos de nombre 'Pend_Archivar' y 'sin_clasificar'.
    '''
    procesados = []
    todos_los_archivos = []

    # Recorrer todos los archivos en la carpeta
    lista_rutas = os.listdir(ruta_carpeta)
    for nombre_archivo in lista_rutas:
        # Comprobar que el archivo sea un PDF
        if nombre_archivo.endswith('.pdf') or nombre_archivo.endswith('.PDF'):
            # Guarda el nombre del archivo en una lista
            todos_los_archivos.append(nombre_archivo)
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            # Leer el contenido del PDF
            with open(ruta_archivo, 'rb') as archivo_pdf:
                lector_pdf = PyPDF2.PdfReader(archivo_pdf)
                texto_completo = ''
                # Extraer el texto de cada página del PDF
                for num_pagina in range(len(lector_pdf.pages)):
                    pagina = lector_pdf.pages[num_pagina]
                    texto_completo += pagina.extract_text()
                # Buscar las palabras en el texto 
                for palabra in proveedores:
                    if palabra in texto_completo:
                        print(f'La palabra "{palabra}" fue encontrada en el archivo "{nombre_archivo}".')
                        # Añade a una lista el archivo de proveedor reconocido
                        procesados.append(nombre_archivo)
                        if palabra == 'V-Valley':
                            # Procesado de facturas de V-Valley
                            # Extracción de datos
                            data = extract_vvalley_data(texto_completo)
                            # Copia y cambio de nombre
                            nombre_nuevo_archivo = crear_nombre_factura_vvalley(data)
                            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/Pend_Archivar', nombre_nuevo_archivo)
                        if palabra == 'INGRAM':
                            # Procesado de facturas de INGRAM
                            data = extract_ingram_data(texto_completo)
                            # Copia y cambio de nombre del archivo
                            nombre_nuevo_archivo = crear_nombre_factura_ingram(data)
                            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/Pend_Archivar', nombre_nuevo_archivo)
                        if palabra == 'Repsol':
                            # Procesado de facturas de Repsol
                            # Copia del archivo sin cambiar el nombre
                            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/Pend_Archivar', nombre_archivo)
    # Procesado de archivos de proveedor desconocido
    print('Copiando archivos no reconocidos')
    # Recorrido de todos los archivos que había originalmente
    for nombre_archivo in todos_los_archivos:
        # Busca archivos que no han sido procesados hasta ahora
        if nombre_archivo not in procesados:
            # Copia del archivo a la carpeta 'sin_clasificar'
            copiar_y_renombrar_pdf(ruta_carpeta, nombre_archivo, ruta_carpeta + '/sin_clasificar', nombre_archivo)
                        

