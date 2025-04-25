import flet as ft
import psutil
import time
import threading


class NetworkSpeedApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Monitor de Velocidad de Red"
        self.page.window_width = 400
        self.page.window_height = 250

        self.download_text = ft.Text("Velocidad de descarga: 0 KB/s", size=18)
        self.upload_text = ft.Text("Velocidad de subida: 0 KB/s", size=18)

        self.page.add(
            ft.Column(
                [
                    ft.Text("Monitoreo de red", size=22, weight=ft.FontWeight.BOLD),
                    self.download_text,
                    self.upload_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

        threading.Thread(target=self.monitor_speed, daemon=True).start()

    def monitor_speed(self):
        old_sent = psutil.net_io_counters().bytes_sent
        old_recv = psutil.net_io_counters().bytes_recv

        while True:
            time.sleep(1)
            new_sent = psutil.net_io_counters().bytes_sent
            new_recv = psutil.net_io_counters().bytes_recv

            upload_speed = (new_sent - old_sent) / 1024  # KB/s
            download_speed = (new_recv - old_recv) / 1024  # KB/s

            old_sent, old_recv = new_sent, new_recv

            self.download_text.value = (
                f"Velocidad de descarga: {download_speed:.2f} KB/s"
            )
            self.upload_text.value = f"Velocidad de subida: {upload_speed:.2f} KB/s"
            self.page.update()


def main(page: ft.Page):
    NetworkSpeedApp(page)


ft.app(target=main)
