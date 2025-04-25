import flet as ft
from frontend.componets.container import CustomContainer
from frontend.componets.text_field import CustomTextField
from frontend.componets.elebate_button import CustomElevatedButton
from frontend.componets.container_page import CustomControllerBasePage
from .base_view import View


class SettingsView(View):
    def __init__(self, page: ft.Page):
        self.page = page
        self._init_ui_components()
        self.init_views

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
            hint_text="Dirección del servidor ",
            disabled=False,
            validation_func=self._validate_server,
            width=200,
        )

        # Puerto del servidor remoto
        self.remote_port_field = CustomTextField(
            label="Puerto Remoto",
            hint_text="Puerto Remoto",
            text_size=4,
            disabled=False,
            validation_func=self._validate_port,
            width=100,
        )

        # Servidor local
        self.local_server_field = CustomTextField(
            label="Servidor Local",
            hint_text="Dirección del servidor local",
            disabled=False,
            validation_func=self._validate_server,
            width=200,
        )

        # Puerto del servidor local
        self.local_port_field = CustomTextField(
            label="Puerto Local",
            hint_text="Puerto del servidor local",
            disabled=False,
            validation_func=self._validate_port,
            width=100,
        )

        # Dominio Proxy
        self.proxy_domain_field = CustomTextField(
            label="Dominio Proxy",
            hint_text="Dominio del servidor proxy",
            disabled=False,
            validation_func=self._validate_domain,
            width=310,
        )

        # Exclusiones
        self.exclusions_field = CustomTextField(
            label="Exclusiones",
            hint_text="Dominios excluidos (separados por comas)",
            disabled=False,
            multiline=True,
            min_lines=2,
            max_lines=4,
            height=100,
            validation_func=self._validate_exclusions,
            width=310,
        )

        # Botón guardar
        self.save_button = CustomElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.SAVE),
                    ft.Text("Guardar Configuración", size=5, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_500,
            ),
            width=200,
            height=40,
            on_click=self._on_save_click,
        )

    def init_views(self):
        # Aquí puedes inicializar otras vistas o componentes si es necesario

        view_proxy = CustomContainer(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Configuración del Proxy",
                                size=20,
                                bgcolor=ft.Colors.RED_200,
                                weight=ft.FontWeight.BOLD,
                                expand=True,
                            )
                        ],
                        height=100,
                    ),
                    ft.Row(
                        controls=[
                            self.remote_server_field,
                            self.remote_port_field,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.local_server_field,
                            self.local_port_field,
                        ]
                    ),
                    self.proxy_domain_field,
                    self.exclusions_field,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=0,
            margin=0,
        )

        view_system = CustomContainer(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                "sdfgdsgf",
                                size=20,
                                bgcolor=ft.Colors.RED_200,
                                weight=ft.FontWeight.BOLD,
                                expand=True,
                            )
                        ],
                        height=100,
                    ),
                    ft.Row(
                        controls=[
                            self.remote_server_field,
                            self.remote_port_field,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.local_server_field,
                            self.local_port_field,
                        ]
                    ),
                    self.proxy_domain_field,
                    self.exclusions_field,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=0,
            margin=0,
            bgcolor=ft.Colors.RED,
        )

        content_container = ft.Container(
            content=view_proxy,  # Mostrar esta vista por defecto
            bgcolor=ft.colors.BLUE_100,
            alignment=ft.alignment.center,
            expand=True,
        )

        def on_nav_change(e):
            index = e.control.selected_index
            if index == 0:
                content_container.content = view_proxy
                content_container.bgcolor = ft.colors.BLUE_100
            elif index == 1:
                content_container.content = view_system
                content_container.bgcolor = ft.colors.RED
            self.page.update()

        nav_bar = ft.NavigationBar(
            selected_index=0,  # Para que muestre la primera vista al iniciar
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Formulario"),
                ft.NavigationBarDestination(icon=ft.Icons.CHECK, label="Opciones"),
            ],
            on_change=on_nav_change,
        )
        view = CustomContainer(
            content=ft.Column(
                controls=[
                    content_container,
                    nav_bar,
                ],
                expand=True,
            )
        )
        view2 = ft.Column(
            controls=[
                content_container,
                nav_bar,
            ]
        )
        return view2

    def build_ui(self):
        layout = CustomControllerBasePage(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Configuración del Proxy",
                                size=20,
                                bgcolor=ft.Colors.RED_200,
                                weight=ft.FontWeight.BOLD,
                                expand=True,
                            )
                        ],
                        height=100,
                    ),
                    ft.Row(
                        controls=[
                            self.remote_server_field,
                            self.remote_port_field,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.local_server_field,
                            self.local_port_field,
                        ]
                    ),
                    self.proxy_domain_field,
                    self.exclusions_field,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=0,
            margin=0,
        )
        return layout

    def _build_server_section(self):
        return CustomContainer(
            content=ft.Column(
                controls=[
                    self.remote_server_field,
                    self.remote_port_field,
                    self.local_server_field,
                    self.local_port_field,
                    self.proxy_domain_field,
                    self.exclusions_field,
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
            ),
            padding=20,
            border=ft.border.all(1, ft.Colors.GREY_400),
            border_radius=10,
            alignment=ft.alignment.center,
        )

    def _build_submit_section(self):
        return CustomContainer(
            content=self.save_button,
            alignment=ft.alignment.center,
        )

    def _on_save_click(self, e):
        # Aquí implementaremos la lógica para guardar la configuración
        pass
