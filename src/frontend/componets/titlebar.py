import flet as ft
from backend.state import app_data

def create_titlebar(page: ft.Page, controller=None):
    """
    Crea una barra de título personalizada con un menú que se muestra 
    en todas las vistas excepto la de login.
    """
    # Vista actual (por defecto, login)
    current_view = "login"
    
    # Función para cambiar la vista actual
    def set_current_view(view_name):
        nonlocal current_view
        current_view = view_name
        update_titlebar()
        page.update()
    
    # Función para actualizar la barra de título
    def update_titlebar():
        # Mostrar menú si no es login Y el usuario está logueado
        show_menu = current_view != "login" and app_data.is_login and controller is not None
        
        # Actualizar visibilidad del menú
        menu_button.visible = show_menu
    
    # Función para cerrar sesión
    def logout_user():
        app_data.is_login = False
        if controller:
            controller.show_login()
    
    # Crear botón de menú (inicialmente puede estar oculto)
    menu_button = ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        icon_color=ft.Colors.WHITE,
        icon_size=20,
        bgcolor=ft.Colors.INDIGO_500,
        tooltip="Opciones",
        visible=False,  # Inicialmente oculto
        items=[
            ft.PopupMenuItem(
                text="Dashboard",
                on_click=lambda _: controller.show_dashboard() if controller else None,
            ),
            ft.PopupMenuItem(
                text="Ajustes",
                on_click=lambda _: controller.show_settings() if controller else None,
            ),
            ft.PopupMenuItem(
                text="Cambiar Contraseña",
                on_click=lambda _: controller.show_change_password() if controller else None,
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.POWER_SETTINGS_NEW, color=ft.Colors.BLUE_GREY_50),
                        ft.Text("Cerrar Sesión", color=ft.Colors.BLUE_GREY_50, size=14),
                    ],
                    spacing=10,
                ),
                on_click=lambda _: logout_user(),
            ),
        ],
    )
    
    # Crear la barra de título
    titlebar = ft.Container(
        content=ft.Row(
            [
                menu_button,
                ft.WindowDragArea(
                    ft.Container(
                        content=ft.Text(
                            "Proxy App",
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
    
    # Añadir método para cambiar de vista
    titlebar.set_view = set_current_view
    
    return titlebar