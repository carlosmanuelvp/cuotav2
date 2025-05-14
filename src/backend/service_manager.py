from typing import Dict, Optional
from .config_manager import ConfigManager
from .controller_cntlm import CNTLMController
from .cuota_uci import CuotaUCI
from .network_monitor import NetworkMonitor
from .network_speed import NetworkSpeedTester
from .notification_service import NotificationService, NotificationType
from .login import AuthManager


class ServiceManager:
    """Gestor central de todos los servicios del backend"""

    def __init__(self):
        # Inicializar servicios core
        self.config = ConfigManager()
        self.notifications = NotificationService()

        # Servicios de red y sistema
        self.network_monitor = NetworkMonitor(self._on_network_status_change)
        self.speed_tester = NetworkSpeedTester(self._on_speed_test_complete)
        self.cntlm = CNTLMController(self.config)

        # Servicios UCI
        self.auth = AuthManager()
        self.cuota = CuotaUCI()

        # Estado del sistema
        self._system_ready = False

    async def initialize(self):
        """Inicializa todos los servicios"""
        try:
            # Cargar configuración
            network_config = self.config.get_config("network")
            if network_config:
                self.network_monitor.set_check_interval(
                    network_config.get("check_interval", 30)
                )
                self.speed_tester.set_test_interval(
                    network_config.get("speed_test_interval", 3600)
                )

            # Iniciar monitoreo de red
            self.network_monitor.start_monitoring()
            self.speed_tester.start_periodic_testing()

            # Verificar estado de CNTLM
            cntlm_status = self.cntlm.get_service_status()
            if cntlm_status[0]:  # Si está activo
                self.notifications.notify(
                    "Servicio CNTLM iniciado correctamente", NotificationType.SUCCESS
                )

            self._system_ready = True
            return True

        except Exception as e:
            self.notifications.notify(
                f"Error al inicializar servicios: {str(e)}", NotificationType.ERROR
            )
            return False

    def shutdown(self):
        """Detiene todos los servicios de forma segura"""
        try:
            self.network_monitor.stop_monitoring()
            self.speed_tester.stop_periodic_testing()
            self.auth.logout()
            self._system_ready = False

        except Exception as e:
            self.notifications.notify(
                f"Error al detener servicios: {str(e)}", NotificationType.ERROR
            )

    def _on_network_status_change(self, is_connected: bool):
        """Callback para cambios en el estado de la red"""
        status = "conectado" if is_connected else "desconectado"
        self.notifications.notify(f"Estado de red: {status}", NotificationType.INFO)

    def _on_speed_test_complete(self, results: Dict):
        """Callback para resultados de pruebas de velocidad"""
        if "error" in results:
            self.notifications.notify(
                f"Error en prueba de velocidad: {results['error']}",
                NotificationType.ERROR,
            )
        else:
            self.notifications.notify(
                f"Prueba de velocidad completada - Down: {results['download']} Mbps, Up: {results['upload']} Mbps",
                NotificationType.INFO,
            )

    @property
    def is_ready(self) -> bool:
        """Verifica si todos los servicios están inicializados"""
        return self._system_ready

    def get_system_status(self) -> Dict:
        """Obtiene el estado general del sistema"""
        return {
            "system_ready": self._system_ready,
            "network_connected": self.network_monitor.get_connection_status(),
            "cntlm_active": self.cntlm.get_service_status()[0],
            "authenticated": self.auth.is_authenticated,
            "last_speed_test": self.speed_tester.get_last_result(),
        }
