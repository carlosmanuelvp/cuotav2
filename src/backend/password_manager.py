import subprocess
from typing import Tuple


class PasswordManager:
    def __init__(self):
        self.current_user = None

    def change_password(
        self, username: str, current_password: str, new_password: str
    ) -> Tuple[bool, str]:
        """
        Cambia la contraseña del usuario en el sistema
        Returns: (success: bool, message: str)
        """
        try:
            # Verificar la contraseña actual
            verify_cmd = f'echo "{current_password}" | sudo -S -v'
            result = subprocess.run(
                verify_cmd, shell=True, capture_output=True, text=True
            )

            if result.returncode != 0:
                return False, "Contraseña actual incorrecta"

            # Cambiar la contraseña
            change_cmd = (
                f'echo "{current_password}\n{new_password}\n{new_password}" | '
                f"sudo -S passwd {username}"
            )
            result = subprocess.run(
                change_cmd, shell=True, capture_output=True, text=True
            )

            if result.returncode != 0:
                return False, f"Error al cambiar la contraseña: {result.stderr}"

            return True, "Contraseña cambiada exitosamente"

        except Exception as e:
            return False, f"Error inesperado: {str(e)}"

    def validate_password_requirements(self, password: str) -> Tuple[bool, str]:
        """
        Valida que la contraseña cumpla con los requisitos mínimos
        Returns: (valid: bool, message: str)
        """
        if len(password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres"

        if not any(c.isupper() for c in password):
            return False, "La contraseña debe contener al menos una mayúscula"

        if not any(c.islower() for c in password):
            return False, "La contraseña debe contener al menos una minúscula"

        if not any(c.isdigit() for c in password):
            return False, "La contraseña debe contener al menos un número"

        if not any(not c.isalnum() for c in password):
            return False, "La contraseña debe contener al menos un carácter especial"

        return True, "Contraseña válida"
