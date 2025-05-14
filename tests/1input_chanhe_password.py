# archivo: change_password.py

import re
import requests

class User:
    def __init__(self, nombre: str, actual: str, nueva: str, confirmar: str):
        self.nombre = nombre
        self.actual = actual
        self.nueva = nueva
        self.confirmar = confirmar

def validar_contrasena(contrasena: str) -> str | None:
    """
    Valida si la contraseña cumple con las políticas de seguridad.
    Retorna None si es válida, o un mensaje de error si no lo es.
    """
    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not re.search(r'[a-z]', contrasena):
        return "La contraseña debe contener al menos una letra minúscula."
    if not re.search(r'[A-Z]', contrasena):
        return "La contraseña debe contener al menos una letra mayúscula."
    if not re.search(r'[0-9]', contrasena):
        return "La contraseña debe contener al menos un número."
    if not re.search(r'[\W_]', contrasena):
        return "La contraseña debe contener al menos un carácter especial."

    return None

def change_pass(user: User) -> dict:
    """
    Cambia la contraseña del usuario.
    Retorna un diccionario con el resultado de la operación.
    """
    if user.nueva != user.confirmar:
        return {
            'success': False,
            'message': 'Las nuevas contraseñas no coinciden.'
        }

    error = validar_contrasena(user.nueva)
    if error:
        return {
            'success': False,
            'message': error
        }

    url = 'https://drst.uci.cu/change-password'
    data = {
        'user': user.nombre,
        'old': user.actual,
        'new': user.nueva,
        'confirm': user.confirmar,
    }

    try:
        response = requests.post(url, data=data)
        return {
            'success': response.status_code == 200,
            'status_code': response.status_code,
            'message': response.text
        }
    except requests.RequestException as e:
        return {
            'success': False,
            'message': f'Error de conexión: {str(e)}'
        }
