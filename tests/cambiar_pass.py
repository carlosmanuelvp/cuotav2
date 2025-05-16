import requests

class User:
    def __init__(self, nombre, actual, nueva, confirmar):
        self.nombre = nombre
        self.actual = actual
        self.nueva = nueva
        self.confirmar = confirmar

def change_pass(user):
    url = 'https://drst.uci.cu/change-password'
    data = {
        'user': user.nombre,
        'old': user.actual,
        'new': user.nueva,
        'confirm': user.confirmar,
    }
    
    response = requests.post(url, data=data)
    return response

# Ejemplo de uso

respuesta = change_pass(usuario)

print("Status Code:", respuesta.status_code)
print("Response:", respuesta.text)

