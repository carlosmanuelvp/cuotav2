import subprocess
import os
import re
from typing import Tuple, Optional
from .config_manager import ConfigManager


class CNTLMController:
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.service_name = "cntlm"
        self.config_file = "/etc/cntlm.conf"

    def start_service(self) -> Tuple[bool, str]:
        """Inicia el servicio CNTLM"""
        try:
            result = subprocess.run(
                ["sudo", "systemctl", "start", self.service_name],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                return True, "Servicio CNTLM iniciado correctamente"
            return False, f"Error al iniciar CNTLM: {result.stderr}"
        except Exception as e:
            return False, f"Error al iniciar CNTLM: {str(e)}"

    def stop_service(self) -> Tuple[bool, str]:
        """Detiene el servicio CNTLM"""
        try:
            result = subprocess.run(
                ["sudo", "systemctl", "stop", self.service_name],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                return True, "Servicio CNTLM detenido correctamente"
            return False, f"Error al detener CNTLM: {result.stderr}"
        except Exception as e:
            return False, f"Error al detener CNTLM: {str(e)}"

    def get_service_status(self) -> Tuple[bool, str]:
        """Obtiene el estado actual del servicio"""
        try:
            result = subprocess.run(
                ["systemctl", "is-active", self.service_name],
                capture_output=True,
                text=True,
            )
            is_active = result.stdout.strip() == "active"
            status_msg = "activo" if is_active else "inactivo"
            return is_active, f"Servicio CNTLM {status_msg}"
        except Exception as e:
            return False, f"Error al verificar estado: {str(e)}"

    def update_config(
        self,
        username: str,
        domain: str,
        proxy: str,
        password_hash: Optional[str] = None,
    ) -> Tuple[bool, str]:
        """Actualiza la configuración de CNTLM"""
        try:
            # Leer configuración actual
            with open(self.config_file, "r") as f:
                config_content = f.read()

            # Actualizar valores
            config_content = self._update_config_value(
                config_content, "Username", username
            )
            config_content = self._update_config_value(config_content, "Domain", domain)
            config_content = self._update_config_value(config_content, "Proxy", proxy)

            if password_hash:
                config_content = self._update_config_value(
                    config_content, "PassNTLMv2", password_hash
                )

            # Guardar configuración
            with open("/tmp/cntlm.conf.tmp", "w") as f:
                f.write(config_content)

            # Mover archivo con sudo
            result = subprocess.run(
                ["sudo", "mv", "/tmp/cntlm.conf.tmp", self.config_file],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                # Actualizar configuración en el gestor
                self.config_manager.update_config("cntlm.username", username)
                self.config_manager.update_config("cntlm.domain", domain)
                self.config_manager.update_config("cntlm.proxy", proxy)
                return True, "Configuración actualizada correctamente"

            return False, f"Error al actualizar configuración: {result.stderr}"
        except Exception as e:
            return False, f"Error al actualizar configuración: {str(e)}"

    def _update_config_value(self, content: str, key: str, value: str) -> str:
        """Actualiza un valor en el contenido de la configuración"""
        pattern = f"^{key}\\s+.*$"
        replacement = f"{key} {value}"

        if re.search(pattern, content, re.MULTILINE):
            return re.sub(pattern, replacement, content, flags=re.MULTILINE)
        else:
            return f"{content}\n{replacement}"

    def generate_password_hash(self, password: str) -> Tuple[bool, str]:
        """Genera el hash de la contraseña para CNTLM"""
        try:
            result = subprocess.run(
                ["cntlm", "-H"], input=password.encode(), capture_output=True, text=True
            )

            if result.returncode == 0:
                # Extraer el hash NTLMv2
                match = re.search(r"PassNTLMv2\s+(.+)", result.stdout)
                if match:
                    return True, match.group(1)

            return False, "No se pudo generar el hash de la contraseña"
        except Exception as e:
            return False, f"Error al generar hash: {str(e)}"
