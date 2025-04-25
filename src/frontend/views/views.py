import flet as ft


def main(page: ft.Page):
    page.title = "NavigationBar Ejemplo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0

    # === VISTA 1: 4 TextFields y un botón ===
    vista_1 = ft.Column(
        controls=[
            ft.TextField(label="Nombre"),
            ft.TextField(label="Apellido"),
            ft.TextField(label="Correo"),
            ft.TextField(label="Teléfono"),
            ft.ElevatedButton(
                text="Enviar", on_click=lambda e: print("Datos enviados")
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # === VISTA 2: Muchos Checkboxes ===
    vista_2 = ft.Column(
        controls=[
            ft.Checkbox(label="Opción A"),
            ft.Checkbox(label="Opción B"),
            ft.Checkbox(label="Opción C"),
            ft.Checkbox(label="Opción D"),
            ft.Checkbox(label="Opción E"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # === VISTA 3: TextFields + Botón ===
    vista_3 = ft.Column(
        controls=[
            ft.TextField(label="Usuario"),
            ft.TextField(label="Contraseña", password=True),
            ft.ElevatedButton(text="Acceder", on_click=lambda e: print("Login")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Contenedor para mostrar las vistas
    content_container = ft.Container(
        content=vista_1,  # Mostrar esta vista por defecto
        bgcolor=ft.colors.BLUE_100,
        alignment=ft.alignment.center,
        expand=True,
    )

    # Cambiar vista al seleccionar en el NavigationBar
    def on_nav_change(e):
        index = e
        if index == 0:
            content_container.content = vista_1
            content_container.bgcolor = ft.colors.BLUE_100
        elif index == 1:
            content_container.content = vista_2
            content_container.bgcolor = ft.colors.GREEN_100
        elif index == 2:
            content_container.content = vista_3
            content_container.bgcolor = ft.colors.AMBER_100
        page.update()

    # Barra de navegación
    nav_bar = ft.NavigationBar(
        selected_index=0,  # Para que muestre la primera vista al iniciar
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Formulario"),
            ft.NavigationBarDestination(icon=ft.Icons.CHECK, label="Opciones"),
            ft.NavigationBarDestination(icon=ft.Icons.LOGIN, label="Login"),
        ],
        on_change=on_nav_change,
    )

    page.navigation_bar = nav_bar
    page.add(content_container)


ft.app(target=main)
