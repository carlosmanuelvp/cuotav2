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

if __name__ == "__main__":

    print("Bienvenido al cambio de contraseña.")

    nombre_usuario = str(input("Introduce tu nombre de usuario: "))
    contrasena_actual = str(input("Introduce tu contraseña actual: "))
    nueva_contrasena = str(input("Introduce tu nueva contraseña: "))
    confirmar_contrasena = str(input("Confirma tu nueva contraseña: "))

    if nueva_contrasena != confirmar_contrasena:
        print("Error: Las nuevas contraseñas no coinciden. Por favor, inténtalo de nuevo.")
    else:
        usuario = User(nombre_usuario, contrasena_actual, nueva_contrasena, confirmar_contrasena)

        respuesta = change_pass(usuario)

        print("\n--- Respuesta del Servidor ---")
        print("Status Code:", respuesta.status_code)
        print("Response:", respuesta.text)

        if respuesta.status_code == 200:
            print("\n¡Contraseña cambiada exitosamente!")
        else:
            print("\nHubo un problema al cambiar la contraseña. Por favor, revisa la respuesta del servidor para más detalles.")
