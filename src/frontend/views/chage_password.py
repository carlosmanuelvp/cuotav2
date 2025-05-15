import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from frontend.componets.checkbox import CustomCheckbox

from .base_view import View

from frontend.componets.message_manager import MessageManager


class ChangePasswordView(View):

    
    def __init__(self, page: ft.Page,controller=None):
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
        self.confirm_password_field = CustomTextField(
            label="Confirmar Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
            on_change=self._validate_fields,
            # on_blur=self._on_password_blur,
            disabled=False,
        )
        
        self.change_password_button = CustomElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.LOCK),
                    ft.Text("Cambiar Contraseña ", size=16, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.Colors.WHITE   ,
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
                self.message_error,  # Asegúrate de mantenerlo en la misma posición
               
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
        return CustomContainer(content=self.change_password_button, alignment=ft.alignment.center)

    async def _on_login_click(self, e):
        self.controller.show_dashboard()
        #self.message_manager.show_message("login_error")
        
    def _validate_fields(self, e):
        username = self.username_field.value.strip()
        password = self.password_field.value.strip()

        # Habilita el botón solo si ambos campos tienen texto
        self.login_button.disabled = not (username and password)
        self.page.update()
