import requests
import xml.etree.ElementTree as ET
from backend.state import user_data

def obtener_cuota_data(usuario: str, clave: str, dominio: str = "uci.cu") -> dict:
    url = 'https://cuotas.uci.cu/servicios/v1/InetCuotasWS.php?WSDL'
    
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
        response = requests.post(url, data=request_body.encode('utf-8'), verify=False, timeout=10)
        
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            
            cuota_total = int(root.find('.//cuota').text)
            cuota_usada = float(root.find('.//cuota_usada').text)
            
            return {
                "status_code": 200,
                "cuota_total": cuota_total,
                "cuota_usada": cuota_usada,
            }
        else:
            return {
                "status_code": response.status_code,
                "error": "Respuesta no exitosa",
                "response_text": response.text
            }

    except Exception as e:
        return {
            "status_code": 500,
            "error": str(e),
        }
