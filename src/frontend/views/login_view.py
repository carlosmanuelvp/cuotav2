import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from frontend.componets.checkbox import CustomCheckbox
from frontend.componets.container_page import CustomControllerBasePage
from .base_view import View
import asyncio
from frontend.componets.message_manager import MessageManager

# validaciones
from backend.get_cuota import obtener_cuota
from backend.account_validation import validate_account, validate_red
from backend.state import app_data
from backend.state import user_data


class LoginView(View):
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller
        self._init_ui_components()
        self.message_manager = MessageManager(self.message_error, self.page)

    def _init_ui_components(self):
        self.message_error = CustomContainer(
            content=ft.Row(controls=[]),  # Aquí un contenedor vacío con controls
            bgcolor=ft.Colors.RED_300,
            border_radius=10,
            width=300,
            height=50,
            opacity=0,
        )

        self.logo_icon = ft.Image(
            src="src/assets/logo.webp",
            width=190,
            height=190,
            fit=ft.ImageFit.CONTAIN,
        )
        self.username_field = CustomTextField(
            label="Usuario",
            hint_text="Escribe el nombre de usuario",
            prefix_icon=ft.Icons.PERSON,
            on_change=self._validate_fields,
            disabled=False,
        )
        self.password_field = CustomTextField(
            label="Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
            on_change=self._validate_fields,
            # on_blur=self._on_password_blur,
            disabled=False,
        )

        self.save_checkbox = CustomCheckbox(label="Mantener sesión iniciada")
        self.login_button_text = ft.Text(
            "Iniciar Sesión", size=16, weight=ft.FontWeight.BOLD
        )
        self.login_button = CustomElevatedButton(
            content=ft.Row(
                [ft.Icon(ft.Icons.LOGIN), self.login_button_text],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.Colors.INDIGO_500,
                overlay_color=ft.Colors.BLUE_400,
                shadow_color=ft.Colors.BLUE_500,
                bgcolor=ft.Colors.INDIGO_500,
            ),
            width=170,
            height=40,
            on_click=self._on_login_click,
            disabled=True,
        )

    def build_ui(self):
        content = ft.Column(
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

    async def _on_login_click(self, e):
        self.login_button.disabled = True
        self.login_button_text.value = "Autenticando"
        self.page.update()

        await asyncio.sleep(0.1)  # asegura que la UI se actualice

        # Ejecutar la solicitud SOAP en un hilo para no bloquear la UI
        status_code = await asyncio.to_thread(
            obtener_cuota, self.username_field.value, self.password_field.value
        )

        if status_code == 200:
            app_data.is_login = True
            user_data.username = self.username_field.value
            user_data.password = self.password_field.value
            self.controller.show_dashboard()
        elif status_code == 500:
            self.message_manager.show_message("login_error")
        else:
            self.message_manager.show_message("network_error")

        self.login_button.disabled = False
        self.login_button_text.value = "Iniciar Sesión"
        self.page.update()

    def _validate_fields(self, e):
        username = self.username_field.value.strip()
        password = self.password_field.value.strip()

        # Habilita el botón solo si ambos campos tienen texto
        self.login_button.disabled = not (username and password)
        self.page.update()
