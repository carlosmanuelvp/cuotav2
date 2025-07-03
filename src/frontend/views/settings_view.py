import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from frontend.componets.container_page import CustomControllerBasePage
from .base_view import View
from backend.state import proxy_conf
import asyncio
from backend.state import cuota_aviso
from plyer import notification


class SettingsView(View):
    def __init__(self, page: ft.Page):
        self.page = page
        self._init_ui_components()

    def _validate_server(self, value):
        if not value or len(value) < 3:
            return False
        return True

    def _validate_port(self, value):
        if not value:
            return False
        try:
            port = int(value)
            return 0 <= port <= 65535
        except ValueError:
            return False

    def _validate_domain(self, value):
        if not value or len(value) < 4:
            return False
        return True

    def _validate_exclusions(self, value):
        if not value:
            return True  # Las exclusiones pueden estar vacías
        exclusions = [x.strip() for x in value.split(",")]
        return all(len(x) > 0 for x in exclusions)

    def _init_ui_components(self):
        # Servidor remoto
        self.remote_server_field = CustomTextField(
            label="Servidor remoto",
            value=proxy_conf.proxy_server,
            hint_text="Dirección del servidor remoto",
            disabled=True,
            validation_func=self._validate_server,
            width=200,
        )

        # Puerto del servidor remoto
        self.remote_port_field = CustomTextField(
            label="Puerto remoto",
            value=proxy_conf.proxy_port,
            hint_text="Puerto remoto",
            text_size=4,
            disabled=True,
            validation_func=self._validate_port,
            width=100,
        )

        # Servidor local
        self.local_server_field = CustomTextField(
            label="Servidor local",
            value=proxy_conf.listen_server,
            hint_text="Dirección del servidor local",
            disabled=False,
            validation_func=self._validate_server,
            width=200,
        )

        # Puerto del servidor local
        self.local_port_field = CustomTextField(
            label="Puerto local",
            value=proxy_conf.listen_port,
            hint_text="Puerto local",
            disabled=False,
            validation_func=self._validate_port,
            width=100,
        )

        # Dominio Proxy
        self.proxy_domain_field = CustomTextField(
            label="Dominio del proxy",
            value=proxy_conf.domain,
            hint_text="Dominio del servidor proxy",
            disabled=True,
            validation_func=self._validate_domain,
            width=310,
        )

        # Exclusiones
        self.exclusions_field = CustomTextField(
            label="Exclusiones",
            hint_text="Dominios excluidos (separados por comas)",
            disabled=True,
            multiline=True,
            min_lines=2,
            max_lines=4,
            height=100,
            validation_func=self._validate_exclusions,
            width=310,
            value=proxy_conf.no_proxy,
        )
        self.notify_percent_field = CustomTextField(
            label="Notificar cuando el uso alcance (%)",
            hint_text="Ejemplo: 80",
            width=310,
            max_length=6,
            validation_func=lambda v: v.replace('.', '', 1).isdigit() and 0 < float(v) <= 100 if v else False,
        )
        self.notify_megabytes_field = CustomTextField(
            label="Notificar cuando queden (MB)",
            hint_text="Ejemplo: 200",
            width=310,
            max_length=10,
            validation_func=lambda v: v.replace('.', '', 1).isdigit() and float(v) > 0 if v else False,
        )
        self.button = CustomElevatedButton(
            content=ft.Text("Guardar"),
            on_click=self._on_save_click,
            bgcolor=ft.colors.INDIGO_500,
            color=ft.colors.WHITE,
            width=100,
            height=40,
        )

    def build_ui(self):
        content = ft.Column(
            controls=[
                ft.Text("Configuración del proxy", size=20, weight=ft.FontWeight.BOLD),
                self._servior_remoto_section(),
                self._servior_local_section(),
                self.proxy_domain_field,
                self.exclusions_field,
                self.por_minuto_section(),
                self._build_button(),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
        )
        return content

    def _servior_remoto_section(self):
        return CustomContainer(
            content=ft.Row(
                controls=[
                    self.remote_server_field,
                    self.remote_port_field,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=10),
        )

    def _servior_local_section(self):
        return CustomContainer(
            content=ft.Row(
                controls=[
                    self.local_server_field,
                    self.local_port_field,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    def por_minuto_section(self):
        return CustomContainer(
            content=ft.Column(
                controls=[
                    ft.Text("Notificaciones", size=20, weight=ft.FontWeight.BOLD),
                    self.notify_percent_field,
                    self.notify_megabytes_field,
                ],
            ),
            margin=ft.margin.only(
                top=2,
            ),
        )

    def _build_button(self):
        return self.button

    async def _on_save_click(self, e):
        # Validar y guardar los valores
        if self.notify_percent_field.value and not self.notify_percent_field.validation_func(self.notify_percent_field.value):
            self.notify_percent_field.error_text = "Debe ser un número entre 0 y 100"
            self.notify_percent_field.update()
            return
        if self.notify_megabytes_field.value and not self.notify_megabytes_field.validation_func(self.notify_megabytes_field.value):
            self.notify_megabytes_field.error_text = "Debe ser un número mayor que 0"
            self.notify_megabytes_field.update()
            return
        cuota_aviso.umbral_notificacion_porcentaje = float(self.notify_percent_field.value) if self.notify_percent_field.value else None
        cuota_aviso.umbral_notificacion_megas = float(self.notify_megabytes_field.value) if self.notify_megabytes_field.value else None

        self.button.disabled = True
        self.button.content = ft.Row(
            [
                ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=ft.colors.WHITE),
                ft.Text("Guardado", color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        )
        self.button.bgcolor = ft.colors.GREEN_700  # Cambiar color para feedback
        self.button.update()

        # Lanzar o detener tarea de monitoreo según configuración
        if cuota_aviso.umbral_notificacion_porcentaje or cuota_aviso.umbral_notificacion_megas:
            if not hasattr(self, '_notifier_task'):
                self._notifier_task = asyncio.create_task(self._notificar_cuota())
        else:
            if hasattr(self, '_notifier_task'):
                self._notifier_task.cancel()
                del self._notifier_task

    async def _notificar_cuota(self):
        while True:
            await asyncio.sleep(15)
            # Obtener el porcentaje de uso actual y megas restantes
            if user_data.cuota_total and user_data.cuota_usada:
                porcentaje_usado = (user_data.cuota_usada / user_data.cuota_total) * 100
                megas_restantes = user_data.cuota_total - user_data.cuota_usada
                if cuota_aviso.umbral_notificacion_porcentaje and porcentaje_usado >= cuota_aviso.umbral_notificacion_porcentaje:
                    notification.notify(
                        title="Aviso de cuota",
                        message=f"Has alcanzado el {porcentaje_usado:.2f}% de tu cuota.",
                        timeout=5
                    )
                    break  # Solo notificar una vez por configuración
                if cuota_aviso.umbral_notificacion_megas and megas_restantes <= cuota_aviso.umbral_notificacion_megas:
                    notification.notify(
                        title="Aviso de cuota",
                        message=f"Te quedan {megas_restantes:.2f} MB de tu cuota.",
                        timeout=5
                    )
                    break  # Solo notificar una vez por configuración
