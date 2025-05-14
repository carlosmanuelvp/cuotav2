import subprocess
import threading
import time
from typing import Optional, Callable
import requests


class NetworkMonitor:
    def __init__(self, status_callback: Optional[Callable] = None):
        self._running = False
        self._status_callback = status_callback
        self._monitor_thread = None
        self._is_connected = False
        self._last_check = 0
        self._check_interval = 30  # segundos

    def start_monitoring(self):
        """Inicia el monitoreo de la red en un hilo separado"""
        if self._running:
            return

        self._running = True
        self._monitor_thread = threading.Thread(target=self._monitor_loop)
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def stop_monitoring(self):
        """Detiene el monitoreo de la red"""
        self._running = False
        if self._monitor_thread:
            self._monitor_thread.join()

    def _monitor_loop(self):
        """Loop principal de monitoreo"""
        while self._running:
            current_status = self.check_connection()
            if current_status != self._is_connected:
                self._is_connected = current_status
                if self._status_callback:
                    self._status_callback(self._is_connected)

            time.sleep(self._check_interval)

    def check_connection(self) -> bool:
        """Verifica si hay conexión a Internet"""
        try:
            # Primero intentamos hacer ping a Google
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "3", "8.8.8.8"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if result.returncode == 0:
                return True

            # Si el ping falla, intentamos una petición HTTP
            response = requests.get("http://www.google.com", timeout=5)
            return response.status_code == 200
        except:
            return False

    def get_connection_status(self) -> bool:
        """Retorna el estado actual de la conexión"""
        return self._is_connected

    def set_check_interval(self, seconds: int):
        """Configura el intervalo de chequeo"""
        self._check_interval = max(10, seconds)  # mínimo 10 segundos

    def get_network_info(self) -> dict:
        """Obtiene información detallada de la red"""
        try:
            # Obtener información de las interfaces de red
            result = subprocess.run(["ip", "addr"], capture_output=True, text=True)

            return {
                "connected": self._is_connected,
                "interfaces": result.stdout,
                "last_check": self._last_check,
            }
        except Exception as e:
            return {
                "connected": self._is_connected,
                "error": str(e),
                "last_check": self._last_check,
            }
