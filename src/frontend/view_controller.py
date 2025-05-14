import flet as ft
from frontend.views.login_view import LoginView
from frontend.views.dashboard_view import DashboardView
from frontend.views.settings_view import SettingsView
from frontend.componets.titlebar import create_titlebar
from frontend.componets.container_page import CustomControllerBasePage


class frontendController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.window.width = 330
        self.page.window.height = 595
        self.page.padding = 0
        self.title_bar_buttons_hidden = True
        self.title_bar_hidden = True
        self.page.window.title_bar_hidden = True
        self.page.window.title_bar_buttons_hidden = True
        self.page.window.frameless = False
        self.page.bgcolor = ft.Colors.BROWN_50

        self._build_ui()

    def _build_ui(self):
        # Instanciar vistas
        self.login_view = LoginView(self.page)
        self.dashboard_view = DashboardView(self.page)
        self.settings_view = SettingsView(self.page)

        # Contenedores de vistas
        self.login_container = CustomControllerBasePage(
            self.login_view.build_ui(), visible=True
        )
        self.settings_container = CustomControllerBasePage(
            content=self.settings_view.build_ui(), visible=False
        )
        self.dashboard_container = CustomControllerBasePage(
            self.dashboard_view.build_ui(), visible=True
        )

        # Apilar vistas
        self.stack = ft.Stack(
            [
                self.login_container,
                #self.dashboard_container,
                self.settings_container,
            ]
        )

        # Añadir barra de título y stack a la página
        self.page.add(
            create_titlebar(self.page, self),
            self.stack,
        )

    def show_dashboard(self):
        self._hide_all()
        self.dashboard_container.visible = True
        self.page.update()

    def show_login(self):
        self._hide_all()
        self.login_container.visible = True
        self.page.update()

    def show_settings(self):
        self._hide_all()
        self.settings_container.visible = True
        self.page.update()

    def _hide_all(self):
        self.login_container.visible = False
        self.dashboard_container.visible = False
        self.settings_container.visible = False
