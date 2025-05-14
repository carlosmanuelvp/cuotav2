import flet as ft
from frontend.view_controller import frontendController


def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height=650
    page.window.width=450
    page.window.title_bar_hidden=True

    frontendController(page)


if __name__ == "__main__":
    ft.app(target=main)
