import re

clientes = ['afanias', 'mopsa', 'aora', 'macrison', 'isq', 'sanfiz', 'legisfund', 'audiconsulting', 'cualicontrol', '40db','moreno', 'saniscle', 'rödl']

def extract_date_infratech(texto):
    #Extrae las fechas de la factura en formato DD/MM/AA
    # Patrón de fecha en expresión regular
    patron_fecha = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b'
    #Para que coja la fecha completa en formato legible:
    fechas_completas = [match.group() for match in re.finditer(patron_fecha, texto)]
    return fechas_completas

def extract_n_factura_infratech(texto):
    # Extrae el número de factura: 9 dígitos seguidos de la palabra ZITRO
    # Patrón de la expresión regular info@zitroconsultores.com000110
    patron = r'\binfo@zitroconsultores\.com(\d{6})\b'
    # Buscar todas las coincidencias en el texto
    coincidencias = re.findall(patron, texto)
    return coincidencias

def extract_cliente_infratech(texto):
    # Busca el nombre del cliente en la factura - En Infratech lo ponen como imagen así que no se puede extraer con este método
    for i in clientes:
        if i in texto.lower():
            return i
    # Si no encuentra al cliente:
    return 'cliente'

def extract_infratech_data(texto):
    print('Extrayendo datos de Infratech')
    print(texto)
    # Extracción de datos
    proveedor = 'INFRATECH'
    fecha = extract_date_infratech(texto)[0]
    n_factura = extract_n_factura_infratech(texto)[0]
    cliente = extract_cliente_infratech(texto)
    concepto = 'avast' if 'avast' in texto.lower() else 'otro'
    # Lista con los datos necesarios para generar el nombre
    data =[proveedor, fecha, n_factura, cliente, concepto]
    return data

def crear_nombre_factura_infratech(data):
    # Cadena con la fecha en formato AAAAMMDD
    fecha = '20' + data[1][-2:] + data[1][3:5] + data[1][:2]
    # Nombre del archivo con formato estándar
    return fecha + '_INFRATECH_Fac_' + data[2] + '_' + data[3] + '_' + data[4] + '.pdf'

