from abc import ABC, abstractmethod
import flet as ft


class View(ABC):
    def __init__(self, page, controller):
        self.page = page

        self.controller = controller

    @abstractmethod
    def build_ui(self):
        pass

    def refresh(self, reload_data: bool = False):
        if reload_data:
            self.load_data()  # Método abstracto o implementado por vistas
        self.page.update()

    def handle_error(self, message: str, type: str = "error"):
        bgcolor = {
            "error": ft.colors.RED_700,
            "success": ft.colors.GREEN_700,
            "warning": ft.colors.YELLOW_700,
        }.get(type, ft.colors.RED_700)
        self.page.snack_bar = ft.SnackBar(content=ft.Text(message), bgcolor=bgcolor)

    def apply_theme(self):
        return {
            "primary_color": ft.colors.BLUE_700
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.colors.BLUE_200,
            # ...
        }
