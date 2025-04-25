import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from frontend.componets.checkbox import CustomCheckbox
from frontend.componets.container_page import CustomControllerBasePage
from .base_view import View


class LoginView(View):
    def __init__(self, page: ft.Page):
        self.page = page
        self._init_ui_components()

    def _init_ui_components(self):
        self.message_error = CustomContainer(
            content=ft.Text(
                "Error message",
            ),
            bgcolor=ft.Colors.RED_300,
            border_radius=10,
            width=300,
            height=50,
            opacity=0,
        )
        self.logo_icon = ft.Image(
            src="src/assets/icon.png",
            width=170,
            height=170,
            fit=ft.ImageFit.CONTAIN,
        )
        self.username_field = CustomTextField(
            label="Usuario",
            hint_text="Escribe el nombre de usuario",
            prefix_icon=ft.Icons.PERSON,
            # on_blur=self._on_usernmae_blur,
            disabled=False,
        )
        self.password_field = CustomTextField(
            label="Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
            # on_blur=self._on_password_blur,
            disabled=False,
        )
        self.save_checkbox = CustomCheckbox(label="Guardar contraseña")
        self.login_button = CustomElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.LOGIN),
                    ft.Text("Iniciar Sesión", size=16, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_500,
            ),
            width=170,
            height=40,
            on_click=self._on_login_click,
        )

    def build_ui(self):
       
        content=ft.Column(
                controls=[
                    self.message_error,  # Asegúrate de mantenerlo en la misma posición
                    self.logo_icon,
                    self._build_input_section(),
                    self._build_submit_section(),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
           
        return content

    def _build_input_section(self):
        return CustomContainer(
            content=ft.Column(
                controls=[
                    self.username_field,
                    self.password_field,
                    ft.Container(
                        content=self.save_checkbox,
                        alignment=ft.alignment.center,
                        width=250,
                        margin=0,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
            ),
            height=210,
            alignment=ft.alignment.center,
        )

    def _build_submit_section(self):
        ft.alignment.bottom_center
        return CustomContainer(content=self.login_button, alignment=ft.alignment.center)

    def _on_login_click(self, e):
        self.message_error.opacity = 1.0
        self.page.update()
