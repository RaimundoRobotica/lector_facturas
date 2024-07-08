import re

clientes = ['afanias', 'mopsa', 'aora', 'macrison', 'isq', 'sanfiz', 'legisfund', 'audiconsulting', 'cualicontrol', '40db','moreno', 'saniscle', 'rödl']

def extract_date(texto):
    #Extrae las fechas de la factura en formato DD/MM/AA
    # Patrón de fecha en expresión regular
    patron_fecha = r'\b(0[1-9]|[12][0-9]|3[01])\-(0[1-9]|1[0-2])\-\d{4}\b'
    fechas = re.findall(patron_fecha, texto)
    #Para que coja la fecha completa en formato legible:
    fechas_completas = [match.group() for match in re.finditer(patron_fecha, texto)]
    return fechas_completas

def extract_n_factura(texto):
    patron = r'\b(\d{9})ZITRO\b'
    # Buscar todas las coincidencias en el texto
    coincidencias = re.findall(patron, texto)
    return coincidencias

def extract_cliente(texto):
    for i in clientes:
        if i in texto.lower():
            return i
    return ''

def extract_ingram_data(texto):
    print('Extrayendo datos de INGRAM-MICRO')
    #print(texto)
    proveedor = 'INGRAM-MICRO'
    fecha = extract_date(texto)[0]
    n_factura = extract_n_factura(texto)[0]
    cliente = extract_cliente(texto)
    concepto = texto.split()[1]
    data =[proveedor, fecha, n_factura, cliente, concepto.lower()]
    return data

def crear_nombre_factura_ingram(data):
    fecha = '20' + data[1][-2:] + data[1][3:5] + data[1][:2]
    return fecha + '_INGRAM-MICRO_Fac_' + data[2] + '_' + data[3] + '_' + data[4] + '.pdf'