import flet as ft
import asyncio


class MessageManager:
    def __init__(self, container: ft.Container, page: ft.Page):
        self.container = container
        self.page = page

    def show_message(self, message_type: str):
        messages = {
            "login_error": {
                "text": "Usuario o contraseña incorrectos",
                "icon": ft.Icons.ERROR_OUTLINE,
                "bgcolor": ft.Colors.RED_600,
            },
            "network_error": {
                "text": "No esta conectado a la red UCI",
                "icon": ft.Icons.WIFI_OFF,
                "bgcolor": ft.Colors.ORANGE_700,
            },
            "success": {
                "text": "¡Inicio de sesión exitoso!",
                "icon": ft.Icons.CHECK_CIRCLE,
                "bgcolor": ft.Colors.GREEN_600,
            },
            "proxy_success": {
                "text": "Proxy Iniciado correctamente!",
                "icon": ft.Icons.CHECK_CIRCLE,
                "bgcolor": ft.Colors.GREEN_600,
            },
            # creme el de proxy deteniedose
            "proxy_stopped": {
                "text": "Proxy detenido correctamente!",
                "icon": ft.Icons.STOP_CIRCLE_OUTLINED,
                "bgcolor": ft.Colors.RED_600,
            },
            "pass_cambiad": {
                "text": "Contrasena cambiada con exito!",
                "icon": ft.Icons.CHECK_CIRCLE,
                "bgcolor": ft.Colors.GREEN_600,
            },
            "no_cambiada": {
                "text": "Contrasena cambiada con exito!",
                "icon": ft.Icons.CHECK_CIRCLE,
                "bgcolor": ft.Colors.RED_500,
            },
        }

        msg = messages.get(message_type, messages["login_error"])

        # Limpia controles actuales y añade el mensaje nuevo con icono
        self.container.content.controls.clear()
        self.container.content.controls.append(
            ft.Row(
                controls=[
                    ft.Icon(name=msg["icon"], color=ft.Colors.WHITE, size=20),
                    ft.Text(msg["text"], color=ft.Colors.WHITE, size=14),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
        self.container.bgcolor = msg["bgcolor"]
        self.container.opacity = 1.0
        self.page.update()

        async def hide_message():
            await asyncio.sleep(3)
            self.container.opacity = 0.0
            self.page.update()

        asyncio.create_task(hide_message())
