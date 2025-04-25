import flet as ft
from frontend.view_controller import frontendController


def main(page: ft.Page):
    page.title = "Cuota-UCI"
    page.theme_mode = ft.ThemeMode.LIGHT

    frontendController(page)


if __name__ == "__main__":
    ft.app(target=main)
