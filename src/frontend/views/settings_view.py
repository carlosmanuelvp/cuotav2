import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from frontend.componets.container_page import CustomControllerBasePage
from .base_view import View
from backend.state import proxy_conf
import asyncio 
from backend.state import cuota_aviso


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
            label="Servidor Remoto",
            value=proxy_conf.proxy_server,
            hint_text="Dirección del servidor ",
            disabled=True,
            validation_func=self._validate_server,
            width=200,
        )

        # Puerto del servidor remoto
        self.remote_port_field = CustomTextField(
            label="Puerto Remoto",
            value=proxy_conf.proxy_port,
            hint_text="Puerto Remoto",
            text_size=4,
            disabled=True,
            validation_func=self._validate_port,
            width=100,
            
        )

        # Servidor local
        self.local_server_field = CustomTextField(
            label="Servidor Local",
            value=proxy_conf.listen_server,
            hint_text="Dirección del servidor local",
            disabled=False,
            validation_func=self._validate_server,
            width=200,
        )

        # Puerto del servidor local
        self.local_port_field = CustomTextField(
            label="Puerto Local",
            value=proxy_conf.listen_port,
            hint_text="Puerto del servidor local",
            disabled=False,
            validation_func=self._validate_port,
            width=100,
        )

        # Dominio Proxy
        self.proxy_domain_field = CustomTextField(
            label="Dominio Proxy",
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
        self.avisar_minutos=CustomTextField(
            label="Avisar cada",
            hint_text="minutos",
            width=310,
            max_length=2,
            
            validation_func=lambda v: v.isdigit() and int(v) > 0,
        )
        self.porciento=CustomTextField(
            label="Notificar cuando llegue",
            hint_text="Porcentaje",
            max_length=2,  
            width=310,
            
        )
        self.button=CustomElevatedButton(
            content=ft.Text("Guardar"),
            on_click=self._on_save_click,
            bgcolor=ft.colors.INDIGO_500,
            color=ft.colors.WHITE,
            width=100,
            height=40
        )

    def build_ui(self):
        content=ft.Column(
            controls=[
                ft.Text("Configuración del Proxy", size=20, weight=ft.FontWeight.BOLD),
                self._servior_remoto_section(  ),
                self._servior_local_section(  ),
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
                    self.avisar_minutos,
                    self.porciento
                ],
            ),
            margin=ft.margin.only(top=2,),
        )
    
    
    def _build_button(self):
        return self.button
            
        
    async def _on_save_click(self, e):

        cuota_aviso.por_minuto=self.avisar_minutos.value
        cuota_aviso.por_ciento=self.porciento.value 
        
        self.button.disabled = True
        self.button.content = ft.Row(
            [
                ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=ft.colors.WHITE),
                ft.Text("Guardado", color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        )
        self.button.bgcolor = ft.colors.GREEN_700 # Cambiar color para feedback
        self.button.update()
        # self.page.update() # Opcional, button.update() podría ser suficiente

        # 4. Esperar 3 segundos
        await asyncio.sleep(3)
        self.button.content = ft.Row(
            [
                ft.Icon(color=ft.colors.WHITE),
                ft.Text("Guardar", color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        )
        self.button.bgcolor = ft.colors.INDIGO_500
        self.button.disabled = False
        # 5. Restaurar contenido original del botón y habilitarlo
        
        self.button.update()
        