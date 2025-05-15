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
                "icon": ft.icons.ERROR_OUTLINE,
                "bgcolor": ft.colors.RED_600,
            },
            "network_error": {
                "text": "No esta conectado a la red UCI",
                "icon": ft.icons.WIFI_OFF,
                "bgcolor": ft.colors.ORANGE_700,
            },
            "success": {
                "text": "¡Inicio de sesión exitoso!",
                "icon": ft.icons.CHECK_CIRCLE,
                "bgcolor": ft.colors.GREEN_600,
            },
        }

        msg = messages.get(message_type, messages["login_error"])

        # Limpia controles actuales y añade el mensaje nuevo con icono
        self.container.content.controls.clear()
        self.container.content.controls.append(
            ft.Row(
                controls=[
                    ft.Icon(name=msg["icon"], color=ft.colors.WHITE, size=20),
                    ft.Text(msg["text"], color=ft.colors.WHITE, size=14),
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
            await asyncio.sleep(5)
            self.container.opacity = 0.0
            self.page.update()

        asyncio.create_task(hide_message())
