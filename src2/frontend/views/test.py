import flet as ft


class LoginViewPage:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller

    def build_ui(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Login", size=28),
                    ft.TextField(label="Usuario"),
                    ft.TextField(label="Contraseña", password=True),
                    ft.ElevatedButton("Entrar", on_click=self.login),
                ],
                spacing=20,
            ),
            alignment=ft.alignment.center,
        )

    def login(self, e):
        self.controller.show_dashboard()


class MainView:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller

    def build_ui(self):
        return ft.Column(
            [
                ft.Text("Bienvenido al Dashboard", size=24),
                ft.ElevatedButton(
                    "Ir a ajustes", on_click=self.controller.show_settings
                ),
            ],
            spacing=20,
        )


class SettingsView:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller

    def build_ui(self):
        return ft.Column(
            [
                ft.Text("Vista de Ajustes", size=24),
                ft.ElevatedButton(
                    "Volver al Dashboard", on_click=self.controller.show_dashboard
                ),
            ],
            spacing=20,
        )


def create_titlebar(page):
    return ft.Row(
        [ft.Text("Cuota-UCI", size=20, weight=ft.FontWeight.BOLD)],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )


class AppController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.build_ui()

    def build_ui(self):
        self.login_view = LoginViewPage(self.page, self)
        self.dashboard_view = MainView(self.page, self)
        self.settings_view = SettingsView(self.page, self)

        self.login_container = ft.Container(content=self.login_view.build_ui())
        self.dashboard_container = ft.Container(
            content=self.dashboard_view.build_ui(), visible=False
        )
        self.settings_container = ft.Container(
            content=self.settings_view.build_ui(), visible=False
        )

        self.view_stack = ft.Stack(
            [self.login_container, self.dashboard_container, self.settings_container]
        )

        self.page.add(create_titlebar(self.page), self.view_stack)

    def show_dashboard(self, e=None):
        self.login_container.visible = False
        self.settings_container.visible = False
        self.dashboard_container.visible = True
        self.page.update()

    def show_settings(self, e=None):
        self.dashboard_container.visible = False
        self.settings_container.visible = True
        self.page.update()


def main(page: ft.Page):
    page.title = "Cuota-UCI"
    AppController(page)


if __name__ == "__main__":
    ft.app(target=main)
