from pprint import pprint
import requests
import xml.etree.ElementTree as ET
from getpass import getpass

# Pedir credenciales al usuario
usuario = input("Usuario: ")
clave = getpass("Contraseña: ")

# URL del servicio
url = 'https://cuotas.uci.cu/servicios/v1/InetCuotasWS.php?WSDL'

# Cuerpo de la solicitud SOAP con los datos ingresados
request_body = f'''
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <ns0:ObtenerCuota xmlns:ns0="urn:InetCuotasWS">
            <usuario>{usuario}</usuario>
            <clave>{clave}</clave>
            <dominio>uci.cu</dominio>
        </ns0:ObtenerCuota>
    </soap-env:Body>
</soap-env:Envelope>
'''

# Realizar la solicitud con la verificación SSL deshabilitada
response = requests.post(url, data=request_body.encode('utf-8'), verify=False)

# Verificar el código de estado de la respuesta
print("Status Code:", response.status_code)

if response.status_code == 200:
    # Analizar la respuesta XML
    root = ET.fromstring(response.text)

    # Extraer los valores de cuota total y utilizada
    cuota_actual = int(root.find('.//cuota').text)
    cuota_utilizada = float(root.find('.//cuota_usada').text)
    nivel_navegacion = str(root.find('.//nivel_navegacion').text)

    # Calcular el porcentaje de uso
    percent = min(cuota_utilizada / cuota_actual, 1.0)

    # Mostrar resultados
    pprint(nivel_navegacion)
    pprint(cuota_utilizada)

elif response.status_code == 500:
    print(f"Error en la contraseña. Código: {response.status_code}")
else:
    print("Error desconocido.")

