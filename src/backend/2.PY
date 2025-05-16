

import requests
import xml.etree.ElementTree as ET

def obtener_cuota(usuario: str, clave: str):
    url = 'https://cuotas.uci.cu/servicios/v1/InetCuotasWS.php?WSDL'
    dominio = 'uci.cu'

    request_body = f'''
    <soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
        <soap-env:Body>
            <ns0:ObtenerCuota xmlns:ns0="urn:InetCuotasWS">
                <usuario>{usuario}</usuario>
                <clave>{clave}</clave>
                <dominio>{dominio}</dominio>
            </ns0:ObtenerCuota>
        </soap-env:Body>
    </soap-env:Envelope>
    '''

    try:
        response = requests.post(url, data=request_body.encode('utf-8'), verify=False)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            root = ET.fromstring(response.text)
            cuota_actual = int(root.find('.//cuota').text)
            cuota_utilizada = float(root.find('.//cuota_usada').text)

            percent = min(cuota_utilizada / cuota_actual, 1.0)

            print(f"Cuota actual (total): {cuota_actual} MB")
            print(f"Cuota utilizada: {cuota_utilizada} MB")
            print(f"Porcentaje utilizado: {percent * 100:.2f}%")

            return {
                "cuota_total": cuota_actual,
                "cuota_usada": cuota_utilizada,
                "porcentaje_usado": percent
            }
        elif response.status_code==500:
            raise print("credenciales invalidas")
        else:
            print(f"Error: {response.status_code}")
            print("Response Body:", response.text)
            return None
    except Exception as e:
        print("Error al realizar la solicitud:", str(e))
        return None
