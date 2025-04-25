import flet as ft
from frontend.main_view_controller import MainController
from models import AppStatus


def main(page: ft.Page):
    MainController(page)


ft.app(target=main)
