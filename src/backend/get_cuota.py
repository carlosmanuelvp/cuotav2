import requests
import xml.etree.ElementTree as ET


def obtener_cuota(usuario: str, clave: str) -> int:
    url = "https://cuotas.uci.cu/servicios/v1/InetCuotasWS.php?WSDL"
    dominio = "uci.cu"

    request_body = f"""
    <soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
        <soap-env:Body>
            <ns0:ObtenerCuota xmlns:ns0="urn:InetCuotasWS">
                <usuario>{usuario}</usuario>
                <clave>{clave}</clave>
                <dominio>{dominio}</dominio>
            </ns0:ObtenerCuota>
        </soap-env:Body>
    </soap-env:Envelope>
    """

    try:
        response = requests.post(url, data=request_body.encode("utf-8"), verify=False)
        return response.status_code
    except Exception as e:
        print("Error:", e)
        return -1  # código personalizado para excepciones
