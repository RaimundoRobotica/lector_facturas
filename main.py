import fitz
import os
from files import *

emisores_factura = ['vvalley']
clientes = ['afanias', 'mopsa', 'aora', 'macrison', 'isq', 'sanfiz', 'legisfund', 'audiconsulting', 'cualicontrol', '40db','moreno', 'saniscle', 'zitro']
conceptos = ['microsoft365']

def renombrar_archivos_pdf(carpeta):
    archivos = os.listdir(carpeta)
    contador = 1
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_completa) and archivo.lower().endswith('.pdf'):
            # Crear el nuevo nombre del archivo
            nuevo_nombre = f"hola_{contador}.pdf"
            nueva_ruta = os.path.join(carpeta, nuevo_nombre)
            # Renombrar el archivo
            os.rename(ruta_completa, nueva_ruta)
            contador += 1
    print(f"Renombrados {contador-1} archivos PDF.")

def listar_archivos_en_carpeta(carpeta):
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        # Crear la ruta completa del archivo
        ruta_completa = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_completa):
            print(f"Archivo: {archivo}")

listar_archivos_en_carpeta('./')


def leer_pdf(ruta_archivo):
    # Abrir el archivo PDF
    documento = fitz.open(ruta_archivo)
    
    # Inicializar una variable para almacenar el texto
    texto_completo = ""
    
    # Iterar sobre cada página del PDF
    for num_pagina in range(documento.page_count):
        pagina = documento.load_page(num_pagina)  # Cargar la página
        texto = pagina.get_text()  # Extraer el texto de la página
        print(texto)  # Agregar el texto de la página al texto completo
    
    # Cerrar el documento PDF
    documento.close()
    
    return texto_completo

# Ejemplo de uso
ruta_archivo = './prueba.PDF'
texto = leer_pdf(ruta_archivo)
print(texto)
