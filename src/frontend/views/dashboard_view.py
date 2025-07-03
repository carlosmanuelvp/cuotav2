import flet as ft
from frontend.componets.container import CustomContainer
from .base_view import View
from frontend.componets.message_manager import MessageManager
from backend.state import app_data, user_data

# from backend.account_validation import validate_account, validate_red
from backend.get_cuota_for_data import obtener_cuota_data
import asyncio
import psutil


class DashboardView(View):
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller
        self._init_ui_components()
        self.message_manager = MessageManager(self.message_error_dashboard, self.page)
        asyncio.create_task(self.monitor_network_speed())  # <-- Añade esta línea

    def _init_ui_components(self):
        self.message = " d"
        self.stats_icon = ft.Icon(name=ft.Icons.CIRCLE, color=ft.Colors.RED_50, size=20)
        self.message_error_dashboard = CustomContainer(
            content=ft.Row(controls=[]),  # Aquí un contenedor vacío con controls
            bgcolor=ft.Colors.RED_300,
            border_radius=10,
            width=300,
            height=50,
            opacity=0,
        )

        self.progress_ring = ft.ProgressRing(
            color=ft.Colors.INDIGO_500,
            bgcolor="#E0E0E0",
            width=200,
            height=200,
            stroke_width=10,
            value=0.85,
        )

        self.progress_text = ft.Text(
            "0/0", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500
        )

        self.nenwork_speed = ft.Text(
            "0 MB/s",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK45,
        )
        self.play_button = ft.IconButton(
            icon=ft.Icons.PLAY_CIRCLE_FILLED,
            icon_color=ft.Colors.INDIGO_500,
            icon_size=50,
            tooltip="Iniciar monitoreo",
            on_click=self._toggle_play_state,
            style=ft.ButtonStyle(
                animation_duration=300,
            ),
        )
        self._is_playing = False
        self.network_connecte = True

    def build_ui(self):
        content = ft.Column(
            controls=[
                ft.Row(
                    controls=[self._build_icon_connect()],
                    alignment=ft.MainAxisAlignment.END,  # Esto lo alinea a la derecha
                ),
                self.message_error_dashboard,
                self._build_progress_section(),
                self._build_speed_section(),
                self.play_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
        return content

    def _build_icon_connect(self):
        return CustomContainer(
            content=self.stats_icon,
            padding=0,
            margin=0,
        )

    def _build_progress_section(self):
        return CustomContainer(
            content=ft.Stack(
                controls=[self.progress_ring, self.progress_text],
                expand=True,
                alignment=ft.alignment.center,
                width=300,
                height=300,
            ),
            padding=6,
            alignment=ft.alignment.center,
            width=300,
            height=300,
        )

    # cremae una un pequeno contendeor que contenga el texto de la velocidad de red
    def _build_speed_section(self):
        return CustomContainer(
            content=self.nenwork_speed,
            padding=6,
            alignment=ft.alignment.center,
            width=300,
            height=50,
        )

    def _build_icon_section(self):
        return CustomContainer(
            content=self.play_button,
            padding=6,
            alignment=ft.alignment.center,
        )

    async def monitor_network_speed(self):
        old_bytes = psutil.net_io_counters().bytes_recv
        while True:
            await asyncio.sleep(1)
            new_bytes = psutil.net_io_counters().bytes_recv
            speed_mb = (new_bytes - old_bytes) / (1024 * 1024)  # MB/s
            speed_kb = (new_bytes - old_bytes) / 1024  # KB/s
            old_bytes = new_bytes

            if speed_mb >= 1:
                self.nenwork_speed.value = f"{speed_mb:.2f} MB/s"
            else:
                self.nenwork_speed.value = f"{speed_kb:.0f} KB/s"
            self.nenwork_speed.update()

    async def actualizar_cuota(self):
        while app_data.is_connected:
            resultado = await asyncio.to_thread(
                obtener_cuota_data, user_data.username, user_data.password
            )
            if resultado["status_code"] == 200:
                total = resultado["cuota_total"]
                usada = resultado["cuota_usada"]
                porcentaje = min(usada / total, 1.0)

                self.progress_ring.value = porcentaje
                self.progress_text.value = f"{usada:.1f}/{total}"
                self.page.update()
            await asyncio.sleep(5)

    async def _toggle_play_state(self, e):
        if not app_data.is_connected:
            self.stats_icon.color = ft.Colors.GREEN_500
            app_data.is_connected = True
            self.play_button.icon = ft.Icons.STOP_CIRCLE
            self.play_button.tooltip = "Detener  conexion proxy"
            self.play_button.icon_color = ft.Colors.RED_500
            self.message_manager.show_message("proxy_success")

            # Iniciar actualización de cuota
            asyncio.create_task(self.actualizar_cuota())

        else:
            self.stats_icon.color = ft.Colors.RED_500
            app_data.is_connected = False
            self.play_button.icon = ft.Icons.PLAY_CIRCLE_FILLED
            self.play_button.tooltip = "Iniciar conexion proxy"
            self.play_button.icon_color = ft.Colors.INDIGO_500
            self.message_manager.show_message("proxy_stopped")

        self.page.update()
