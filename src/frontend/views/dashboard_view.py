import flet as ft
from frontend.componets.container import CustomContainer
from .base_view import View
from frontend.componets.container_page import CustomControllerBasePage


class DashboardView(View):
    def __init__(self, page: ft.Page):
        self.page = page
        self._init_ui_components()

    def _init_ui_components(self):
        self.message_alert = CustomContainer(
            content=ft.Text(
                "Error message",
            ),
            bgcolor=ft.Colors.RED_300,
            border_radius=10,
            width=300,
            height=50,
            opacity=1,
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
            "60/100", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500
        )

    def build_ui(self):
        layout = CustomControllerBasePage(
            content=ft.Column(
                controls=[
                    self.message_alert,  # Asegúrate de mantenerlo en la misma posición
                    self._build_progress_section(),
                ],
                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=10,
            ),
            padding=0,
            margin=0,
        )
        return layout

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
            bgcolor=ft.Colors.RED_800,
        )
