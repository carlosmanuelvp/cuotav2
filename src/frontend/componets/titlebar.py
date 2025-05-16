import flet as ft


def create_titlebar(
    page: ft.Page, controller=None
):  # Añadimos un argumento para el callback
    titlebar = ft.Container(
        content=ft.Row(
            [
                # Botón de menú de 3 puntos
                ft.PopupMenuButton(
                    icon=ft.Icons.MENU,
                    icon_color=ft.Colors.WHITE,
                    icon_size=20,
                    bgcolor=ft.Colors.INDIGO_500,
                    tooltip="Opciones",
                    items=[
                        ft.PopupMenuItem(
                            text="Ajustes",
                            on_click=lambda _: controller.show_settings()
                            if controller
                            else None,  # Añadido el callback
                        ),
                        ft.PopupMenuItem(
                            text="Cambiar Contraseña",
                            on_click=lambda _: controller.show_change_password()
                            if controller
                            else None,  # Usamos el callback
                        ),
                        ft.PopupMenuItem(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(
                                        ft.icons.POWER_SETTINGS_NEW,
                                        color=ft.Colors.BLUE_GREY_50,
                                    ),  # Icono de salir
                                    ft.Text(
                                        "Salir", color=ft.Colors.BLUE_GREY_50, size=14
                                    ),  # Texto de salir
                                ],
                                spacing=10,  # Espacio entre el icono y el texto
                            ),
                            on_click=lambda _: controller.show_login()
                            if controller
                            else None,
                        ),
                    ],
                ),
                # Área de arrastre con el título centrado
                ft.WindowDragArea(
                    ft.Container(
                        content=ft.Text(
                            "",
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.INDIGO_500,
                        expand=True,
                        margin=0,
                        padding=0,
                    ),
                    expand=True,
                ),
                # Botones minimizar y cerrar
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            icon_size=20,
                            tooltip="Cerrar",
                            on_click=lambda _: page.window.close(),
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.INDIGO_500,
        height=40,
        padding=0,
        margin=0,
    )

    return titlebar
