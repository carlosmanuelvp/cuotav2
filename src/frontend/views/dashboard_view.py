import flet as ft
from frontend.componets.container import CustomContainer
from .base_view import View
from frontend.componets.container_page import CustomControllerBasePage
from backend.models import AppStatus
from frontend.views.login_view import LoginView


class DashboardView(View):
    def __init__(self, page: ft.Page):
        self.page = page
        
        self._init_ui_components()

    def _init_ui_components(self):
        self.message = " d"
        self.message_alert_container = CustomContainer(
            content=ft.Text(
                self.message,
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
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
            value=0.6,
        )
        self.progress_text = ft.Text(
            "600/100", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500
        )

        self.nenwork_speed = ft.Text(
            "144, MB/s",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK45,
        )
        self.play_button = ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE_FILLED,
            icon_color=ft.colors.BLUE_500,
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
                self.message_alert_container,  # Asegúrate de mantenerlo en la misma posición
                self._build_progress_section(),
                self._build_speed_section(),
                self.play_button,
            ],
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
        return content

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

    def _toggle_play_state(self, e):
        if self._is_playing:
            self.play_button.icon = ft.icons.PLAY_CIRCLE_FILLED
            self.play_button.tooltip = "Detener monitoreo"
            self.message_alert_container.opacity = 0
            self.message = "Proxy iniciado correctamente"

        else:
            self.play_button.icon = ft.icons.PLAY_CIRCLE_FILLED
            self.play_button.tooltip = "Iniciar monitoreo"
            self.message_alert_container.opacity = 1
            self.message = "Proxy detenido "

        self.play_button.update()
        self.page.update()
