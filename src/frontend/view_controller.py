import flet as ft
from frontend.views.login_view import LoginView
from frontend.views.dashboard_view import DashboardView
from frontend.views.settings_view import SettingsView
from frontend.views.chage_password import ChangePasswordView
from frontend.componets.titlebar import create_titlebar
from frontend.componets.container_page import CustomControllerBasePage
from backend.state import app_data

class frontendController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.window.width = 330
        self.page.window.height = 595

        self.title_bar_buttons_hidden = True
        self.title_bar_hidden = True
        self.page.window.title_bar_hidden = True
        self.page.window.title_bar_buttons_hidden = True
        self.page.window.frameless = False
        self.page.bgcolor = ft.Colors.BLUE_GREY_50

        self._build_ui()

    def _build_ui(self):
        self.titlebar = create_titlebar(self.page, self)
        # Instanciar vistas
        self.login_view = LoginView(self.page, self)
        self.dashboard_view = DashboardView(self.page, self)
        self.settings_view = SettingsView(self.page)
        self.change_password = ChangePasswordView(self.page, self)
        # Contenedores de vistas
        self.login_container = CustomControllerBasePage(
            self.login_view.build_ui(), visible=True, padding=0, margin=0
        )
        self.settings_container = CustomControllerBasePage(
            content=self.settings_view.build_ui(), visible=False, padding=0, margin=0
        )
        self.dashboard_container = CustomControllerBasePage(
            self.dashboard_view.build_ui(), visible=False, padding=0
        )
        self.change_password_container = CustomControllerBasePage(
            content=self.change_password.build_ui(), visible=False, padding=0, margin=0
        )
        # Apilar vistas
        self.stack = ft.Stack(
            [
                self.login_container,
                self.dashboard_container,
                self.settings_container,
                self.change_password_container,
            ],
        )

        # Añadir barra de título y stack a la página
        self.page.add(
            ft.Column(
                [
                    self.titlebar,  # Barra de título siempre presente
                    ft.Container(  # Contenedor para las vistas
                        content=ft.Stack(
                            [
                                self.login_container,
                                self.dashboard_container,
                                self.settings_container,
                                self.change_password_container,
                            ]
                        ),
                        expand=True,
                    )
                ],
                spacing=0,
                expand=True,
            )
        )

    def show_dashboard(self):
        self.titlebar.set_view("dashboard")
        self._hide_all()
        self.dashboard_container.visible = True
        self.page.update()

    def show_login(self):
        self.titlebar.set_view("login")
        app_data.is_login = False
        self._hide_all()
        self.login_container.visible = True

        self.page.update()

    def show_settings(self):
        self._hide_all()
        self.settings_container.visible = True
        self.page.update()

    def show_change_password(self):
        self._hide_all()
        self.change_password_container.visible = True
        self.page.update()

    def _hide_all(self):
        self.change_password_container.visible = False
        self.login_container.visible = False
        self.dashboard_container.visible = False
        self.settings_container.visible = False
