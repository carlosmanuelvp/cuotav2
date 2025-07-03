from sys import version_info
import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from backend.cambiar_pass import change_pass
from backend.state import user_data

from .base_view import View
import asyncio
from frontend.componets.message_manager import MessageManager


class ChangePasswordView(View):
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

        self.current_password = CustomTextField(
            label="Contrasena Actual",
            hint_text="Escribe la contrasena actual",
            # prefix_icon=ft.Icons.PERSON,
            on_change=self._validate_fields_current_password,
            disabled=False,
            error_text=None,
            can_reveal_password=True,
            password=True,
        )
        self.password_field = CustomTextField(
            label="Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            # prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
            on_change=self._validate_fields,
            # on_blur=self._on_password_blur,
            disabled=False,
        )
        self.confirm_password_field = CustomTextField(
            label="Confirmar Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            # prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
            on_change=self._validate_fields,
            # on_blur=self._on_password_blur,
            disabled=False,
        )
        # creae un variebla para mayor de 8 caracterees
        self.mayor_eight_digitos = ft.Text(
            "más de 8 de caracteres", color=ft.Colors.RED_ACCENT_700, size=18
        )
        self.icon_eight_digitos = ft.Icon(
            ft.Icons.CHECK_CIRCLE, color=ft.Colors.RED_ACCENT_700, size=18
        )

        # Validación de al menos 1 mayúscula
        self.mayuscula_text = ft.Text(
            "Al menos 1 mayúscula", color=ft.Colors.RED_ACCENT_700, size=18
        )
        self.icon_mayuscula = ft.Icon(
            ft.Icons.CHECK_CIRCLE, color=ft.Colors.RED_ACCENT_700, size=18
        )

        # Validación de al menos 1 minúscula
        self.minuscula_text = ft.Text(
            "Al menos 1 minúscula", color=ft.Colors.RED_ACCENT_700, size=18
        )
        self.icon_minuscula = ft.Icon(
            ft.Icons.CHECK_CIRCLE, color=ft.Colors.RED_ACCENT_700, size=18
        )

        # Validación de al menos 1 dígito
        self.digito_text = ft.Text(
            "Al menos 1 dígito", color=ft.Colors.RED_ACCENT_700, size=18
        )
        self.icon_digito = ft.Icon(
            ft.Icons.CHECK_CIRCLE, color=ft.Colors.RED_ACCENT_700, size=18
        )

        # Validación de al menos 1 caracter especial
        self.caracter_especial_text = ft.Text(
            "Al menos 1 caracter especial", color=ft.Colors.RED_ACCENT_700, size=18
        )
        self.icon_caracter_especial = ft.Icon(
            ft.Icons.CHECK_CIRCLE, color=ft.Colors.RED_ACCENT_700, size=18
        )

        self.login_button = CustomElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.LOGIN),
                    ft.Text("Cambiar", size=16, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.Colors.WHITE,
                overlay_color=ft.Colors.BLUE_400,
                shadow_color=ft.Colors.BLUE_500,
                bgcolor=ft.Colors.BLUE_500,
            ),
            width=170,
            height=40,
            on_click=self._on_login_click,
            disabled=True,
        )

    def build_ui(self):
        content = ft.Column(
            controls=[
                self._build_input_section(),
                self._build_requisitos_section(),
                self.message_error,  #
                self._build_submit_section(),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,

        )

        return content

    def _build_requisitos_section(self):
        return CustomContainer(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.icon_eight_digitos,
                            self.mayor_eight_digitos,
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear fila al inicio (izquierda)
                    ),
                    ft.Row(
                        controls=[
                            self.icon_mayuscula,
                            self.mayuscula_text,
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear fila al inicio (izquierda)
                    ),
                    ft.Row(
                        controls=[
                            self.icon_minuscula,
                            self.minuscula_text,
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear fila al inicio (izquierda)
                    ),
                    ft.Row(
                        controls=[
                            self.icon_digito,
                            self.digito_text,
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear fila al inicio (izquierda)
                    ),
                    ft.Row(
                        controls=[
                            self.icon_caracter_especial,
                            self.caracter_especial_text,
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear fila al inicio (izquierda)
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,  # Alinear columna horizontalmente al inicio
                alignment=ft.MainAxisAlignment.START,  # Alinear columna verticalmente al inicio
                spacing=5,  # Espaciado entre filas para mejor visualización
            ),
            alignment=ft.alignment.center_left,  # Alinear el contenedor a la izquierda
            width=300,  # Ancho fijo para mejor control
            padding=ft.padding.only(
                left=30, top=6, bottom=10
            ),  # Padding asimétrico para ajustar la posición
            border_radius=8,
            # Bordes redondeados para mejor apariencia
        )

    def _build_input_section(self):
        return CustomContainer(
            content=ft.Column(
                controls=[
                    self.current_password,
                    self.password_field,
                    self.confirm_password_field,
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
        return CustomContainer(
            content=self.login_button,
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=46),
        )
        # Añadir un margen superior para separar del resto de los campos

    async def _on_login_click(self, e):
        self.login_button.disabled = True
        self.page.update()

        await asyncio.sleep(0.1)

        status_code = await asyncio.to_thread(lambda: change_pass(
        user_data.username,
        self.current_password.value,
        self.password_field.value,
        self.confirm_password_field.value,
    ))


        if status_code == 200:
            self.message_manager.show_message("pass_cambiad")
        if status_code == 401:
            self.message_manager.show_message("no_cambiada")
        self.login_button.disabled = False
        self.page.update()

    def _validate_fields_current_password(self, e):
        current_password_ = self.current_password.value.strip()

        # Validación del campo de contraseña actual
        if not current_password_:
            self.current_password.error_text = "No puede estar vacía"
        else:
            self.current_password.error_text = None

        self.page.update()

    def _validate_fields(self, e):
        # Obtener valores y eliminar espacios
        current_password = (
            self.current_password.value.strip() if self.current_password.value else ""
        )
        new_password = (
            self.password_field.value.strip() if self.password_field.value else ""
        )
        confirm_password = (
            self.confirm_password_field.value.strip()
            if self.confirm_password_field.value
            else ""
        )

        # Verificar que la contraseña actual no esté vacía
        if not current_password:
            self.current_password.error_text = "no puede estar vacía"
        else:
            self.current_password.error_text = None

        # Verificar que la nueva contraseña no sea igual a la actual
        if new_password and current_password and new_password == current_password:
            self.password_field.error_text = "debe ser diferente a la actual"
        else:
            self.password_field.error_text = None

        # Verificar que la confirmación coincida con la nueva contraseña
        if confirm_password and new_password != confirm_password:
            self.confirm_password_field.error_text = "Las contraseñas no coinciden"
        else:
            self.confirm_password_field.error_text = None

        # NUEVA SECCIÓN: Validar requisitos de contraseña
        if new_password:
            # 1. Verificar longitud mínima (8 caracteres)
            has_length = len(new_password) >= 8
            self.icon_eight_digitos.name = (
                ft.Icons.CHECK_CIRCLE if has_length else ft.Icons.CANCEL
            )
            self.icon_eight_digitos.color = (
                ft.Colors.GREEN_600 if has_length else ft.Colors.RED_ACCENT_700
            )
            self.mayor_eight_digitos.color = (
                ft.Colors.GREEN_600 if has_length else ft.Colors.RED_ACCENT_700
            )

            # 2. Verificar al menos una mayúscula
            has_uppercase = any(c.isupper() for c in new_password)
            self.icon_mayuscula.name = (
                ft.Icons.CHECK_CIRCLE if has_uppercase else ft.Icons.CANCEL
            )
            self.icon_mayuscula.color = (
                ft.Colors.GREEN_600 if has_uppercase else ft.Colors.RED_ACCENT_700
            )
            self.mayuscula_text.color = (
                ft.Colors.GREEN_600 if has_uppercase else ft.Colors.RED_ACCENT_700
            )

            # 3. Verificar al menos una minúscula
            has_lowercase = any(c.islower() for c in new_password)
            self.icon_minuscula.name = (
                ft.Icons.CHECK_CIRCLE if has_lowercase else ft.Icons.CANCEL
            )
            self.icon_minuscula.color = (
                ft.Colors.GREEN_600 if has_lowercase else ft.Colors.RED_ACCENT_700
            )
            self.minuscula_text.color = (
                ft.Colors.GREEN_600 if has_lowercase else ft.Colors.RED_ACCENT_700
            )

            # 4. Verificar al menos un dígito
            has_digit = any(c.isdigit() for c in new_password)
            self.icon_digito.name = (
                ft.Icons.CHECK_CIRCLE if has_digit else ft.Icons.CANCEL
            )
            self.icon_digito.color = (
                ft.Colors.GREEN_600 if has_digit else ft.Colors.RED_ACCENT_700
            )
            self.digito_text.color = (
                ft.Colors.GREEN_600 if has_digit else ft.Colors.RED_ACCENT_700
            )

            # 5. Verificar al menos un carácter especial
            special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
            has_special = any(c in special_chars for c in new_password)
            self.icon_caracter_especial.name = (
                ft.Icons.CHECK_CIRCLE if has_special else ft.Icons.CANCEL
            )
            self.icon_caracter_especial.color = (
                ft.Colors.GREEN_600 if has_special else ft.Colors.RED_ACCENT_700
            )
            self.caracter_especial_text.color = (
                ft.Colors.GREEN_600 if has_special else ft.Colors.RED_ACCENT_700
            )

            # Verificar todos los requisitos para habilitar el botón
            password_valid = (
                has_length
                and has_uppercase
                and has_lowercase
                and has_digit
                and has_special
            )
        else:
            # Si no hay contraseña, todos los indicadores en rojo
            for icon, text in [
                (self.icon_eight_digitos, self.mayor_eight_digitos),
                (self.icon_mayuscula, self.mayuscula_text),
                (self.icon_minuscula, self.minuscula_text),
                (self.icon_digito, self.digito_text),
                (self.icon_caracter_especial, self.caracter_especial_text),
            ]:
                icon.name = ft.Icons.CANCEL
                icon.color = ft.Colors.RED_ACCENT_700
                text.color = ft.Colors.RED_ACCENT_700

            password_valid = False

        # Habilitar el botón solo si todas las condiciones se cumplen
        self.login_button.disabled = not (
            current_password
            and new_password
            and confirm_password
            and new_password != current_password
            and new_password == confirm_password
            and password_valid  # Añadir esta condición
        )

        self.page.update()
