import speedtest
import threading
from typing import Dict, Optional, Callable
import time


class NetworkSpeedTester:
    def __init__(self, callback: Optional[Callable[[Dict], None]] = None):
        self._speed_test = speedtest.Speedtest()
        self._callback = callback
        self._running = False
        self._test_thread = None
        self._last_result = None
        self._test_interval = 3600  # 1 hora por defecto

    def start_periodic_testing(self):
        """Inicia las pruebas periódicas de velocidad"""
        if self._running:
            return

        self._running = True
        self._test_thread = threading.Thread(target=self._periodic_test_loop)
        self._test_thread.daemon = True
        self._test_thread.start()

    def stop_periodic_testing(self):
        """Detiene las pruebas periódicas"""
        self._running = False
        if self._test_thread:
            self._test_thread.join()

    def _periodic_test_loop(self):
        """Loop principal para pruebas periódicas"""
        while self._running:
            self.test_speed()
            time.sleep(self._test_interval)

    def test_speed(self) -> Dict:
        """
        Realiza una prueba de velocidad
        Returns: Dict con los resultados (download_speed, upload_speed, ping)
        """
        try:
            print("Testeando servidores...")
            self._speed_test.get_best_server()

            print("Midiendo velocidad de descarga...")
            download_speed = self._speed_test.download() / 1_000_000  # Convertir a Mbps

            print("Midiendo velocidad de subida...")
            upload_speed = self._speed_test.upload() / 1_000_000  # Convertir a Mbps

            ping = self._speed_test.results.ping

            self._last_result = {
                "download": round(download_speed, 2),
                "upload": round(upload_speed, 2),
                "ping": round(ping, 2),
                "timestamp": time.time(),
            }

            if self._callback:
                self._callback(self._last_result)

            return self._last_result

        except Exception as e:
            error_result = {"error": str(e), "timestamp": time.time()}
            if self._callback:
                self._callback(error_result)
            return error_result

    def get_last_result(self) -> Optional[Dict]:
        """Retorna el último resultado de la prueba de velocidad"""
        return self._last_result

    def set_test_interval(self, seconds: int):
        """Configura el intervalo entre pruebas"""
        self._test_interval = max(300, seconds)  # mínimo 5 minutos
