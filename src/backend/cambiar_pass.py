import requests


def change_pass(nombre, actual, nueva, confirmar):
    url = "https://drst.uci.cu/change-password"
    data = {
        "user": nombre,
        "old": actual,
        "new": nueva,
        "confirm": confirmar,
    }

    try:
        response = requests.post(url, data=data)
        print(response.status_code)
        return response.status_code
    except requests.RequestException:
        return -1  # Código para error de red


# Ejemplo de uso
