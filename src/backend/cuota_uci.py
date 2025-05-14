import requests
from typing import Dict, Optional, Tuple
import re


class CuotaUCI:
    def __init__(self):
        self.base_url = "https://portal.uci.cu"
        self.cuota_url = f"{self.base_url}/cuota"
        self._session = requests.Session()

    def get_cuota(self, username: str, password: str) -> Tuple[bool, Dict]:
        """
        Obtiene la información de cuota del usuario
        Returns: (success: bool, data: Dict)
        """
        try:
            # Iniciar sesión
            login_data = {"username": username, "password": password}

            response = self._session.post(
                f"{self.base_url}/login",
                data=login_data,
                verify=False,  # Para certificados auto-firmados
            )

            if not response.ok:
                return False, {"error": "Error de autenticación"}

            # Obtener página de cuota
            response = self._session.get(self.cuota_url, verify=False)
            if not response.ok:
                return False, {"error": "Error al obtener la información de cuota"}

            # Extraer información de cuota mediante regex
            cuota_info = self._parse_cuota_page(response.text)
            if not cuota_info:
                return False, {"error": "No se pudo extraer la información de cuota"}

            return True, cuota_info

        except requests.RequestException as e:
            return False, {"error": f"Error de conexión: {str(e)}"}
        except Exception as e:
            return False, {"error": f"Error inesperado: {str(e)}"}
        finally:
            self._session.close()

    def _parse_cuota_page(self, html_content: str) -> Optional[Dict]:
        """Extrae la información de cuota del HTML"""
        try:
            # Patrones para extraer la información (ajustar según el HTML real)
            patterns = {
                "cuota_total": r"Cuota total:\s*(\d+(?:\.\d+)?)\s*MB",
                "cuota_usada": r"Cuota usada:\s*(\d+(?:\.\d+)?)\s*MB",
                "cuota_restante": r"Cuota restante:\s*(\d+(?:\.\d+)?)\s*MB",
                "tiempo_activo": r"Tiempo activo:\s*(\d+:\d+:\d+)",
            }

            result = {}
            for key, pattern in patterns.items():
                match = re.search(pattern, html_content)
                if match:
                    value = match.group(1)
                    # Convertir valores numéricos
                    if key in ["cuota_total", "cuota_usada", "cuota_restante"]:
                        value = float(value)
                    result[key] = value

            if result:
                # Calcular porcentaje usado
                if "cuota_total" in result and "cuota_usada" in result:
                    result["porcentaje_usado"] = round(
                        (result["cuota_usada"] / result["cuota_total"]) * 100, 2
                    )
                return result

            return None

        except Exception:
            return None

    def logout(self):
        """Cierra la sesión en el portal"""
        try:
            self._session.get(f"{self.base_url}/logout", verify=False)
        except:
            pass  # Ignorar errores al cerrar sesión
        finally:
            self._session.close()
