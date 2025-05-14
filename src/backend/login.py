import requests
from typing import Tuple, Dict, Optional
from datetime import datetime
from .models import User


class AuthManager:
    def __init__(self):
        self._session = requests.Session()
        self.current_user: Optional[User] = None
        self._last_login: Optional[datetime] = None
        self._is_authenticated = False

    async def login(self, username: str, password: str) -> Tuple[bool, str]:
        """Autenticar usuario contra el portal UCI"""
        try:
            # Intentar autenticación contra el portal
            response = self._session.post(
                "https://portal.uci.cu/login",
                data={"username": username, "password": password},
                verify=False,  # Para certificados auto-firmados
            )

            if response.ok:
                self.current_user = User(username=username, password=password)
                self._last_login = datetime.now()
                self._is_authenticated = True
                return True, "Autenticación exitosa"

            return False, "Credenciales inválidas"

        except requests.RequestException as e:
            return False, f"Error de conexión: {str(e)}"
        except Exception as e:
            return False, f"Error inesperado: {str(e)}"

    def logout(self) -> None:
        """Cerrar sesión del usuario actual"""
        if self._is_authenticated:
            try:
                self._session.get("https://portal.uci.cu/logout", verify=False)
            except:
                pass  # Ignorar errores al cerrar sesión
            finally:
                self._session.close()
                self.current_user = None
                self._last_login = None
                self._is_authenticated = False

    @property
    def is_authenticated(self) -> bool:
        """Verificar si hay una sesión activa"""
        return self._is_authenticated

    @property
    def last_login(self) -> Optional[datetime]:
        """Obtener la fecha/hora del último login exitoso"""
        return self._last_login

    def get_session_info(self) -> Dict:
        """Obtener información de la sesión actual"""
        return {
            "is_authenticated": self._is_authenticated,
            "username": self.current_user.username if self.current_user else None,
            "last_login": self._last_login.isoformat() if self._last_login else None,
        }
