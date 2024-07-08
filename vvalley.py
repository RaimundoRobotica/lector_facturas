import re

# Posibles clientes para este proveedor
clientes = ['afanias', 'mopsa', 'aora', 'macrison', 'isq', 'sanfiz', 'legisfund', 'audiconsulting', 'cualicontrol', '40db','moreno', 'saniscle']

def extract_date(texto):
    #Extrae las fechas de la factura en formato DD/MM/AA
    # Patrón de fecha en expresión regular
    patron_fecha = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{2}\b'
    # Fecha completa en formato legible:
    fechas_completas = [match.group() for match in re.finditer(patron_fecha, texto)]
    return fechas_completas

def extract_n_factura(texto):
    # Una letra en mayúscula seguida de 9 dígitos
    patron = r'\b[A-Z]\d{9}\b'
    # Buscar todas las coincidencias en el texto
    coincidencias = re.findall(patron, texto)
    return coincidencias

def extract_cliente(texto):
    # Búsqueda de posibles clientes
    for i in clientes:
        if i in texto.lower():
            return i
    # Si no se encuentra, el cliente es zitro
    return 'zitro'

def extract_vvalley_data(texto):
    print('Extrayendo datos de V-Valley')
    #print(texto)
    # Extracción de datos necesarios
    proveedor = 'VVALLEY'
    fecha = extract_date(texto)[0]
    n_factura = extract_n_factura(texto)[0]
    cliente = extract_cliente(texto)
    concepto = ['microsoft365' if 'microsoft' in texto.lower() else 'otro'][0]
    #lista con datos necesarios para generar el nombre
    data =[proveedor, fecha, n_factura, cliente, concepto]
    return data

def crear_nombre_factura_vvalley(data):
    # Fecha en formato AAAAMMDD
    fecha = '20' + data[1][-2:] + data[1][3:5] + data[1][:2]
    # Generación de nombre del archivo
    return fecha + '_VVALLEY_Fac_' + data[2] + '_' + data[3] + '_' + data[4] + '.pdf'
