import requests
import xml.etree.ElementTree as ET

# URL and request body
url = 'https://cuotas.uci.cu/servicios/v1/InetCuotasWS.php?WSDL'
request_body = '''
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <ns0:ObtenerCuota xmlns:ns0="urn:InetCuotasWS">
            <usuario>carlosmvp</usuario>
            <clave>Contreras28.00</clave>
            <dominio>uci.cu</dominio>
        </ns0:ObtenerCuota>
    </soap-env:Body>
</soap-env:Envelope>
'''

# Make the request with SSL verification disabled
response = requests.post(url, data=request_body.encode('utf-8'), verify=False)

# Check the status code
print("Status Code:", response.status_code)

# Process the response if status code is 200
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.text)

    # Extract the cuota (total) and cuota_usada (used) from the XML
    cuota_actual = int(root.find('.//cuota').text)
    cuota_utilizada = float(root.find('.//cuota_usada').text)

    # Calculate the percentage of the used quota
    if cuota_utilizada > cuota_actual:
        percent = 1.0
    else:
        percent = cuota_utilizada / cuota_actual

    # Print the results
    print(f"Cuota actual (total): {cuota_actual} MB")
    print(f"Cuota utilizada: {cuota_utilizada} MB")
    print(f"Porcentaje utilizado: {percent * 100:.2f}%")
else:
    print(f"Error: {response.status_code}")
    print("Response Body:", response.text)
