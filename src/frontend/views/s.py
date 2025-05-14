import flet as ft

def main(page: ft.Page):
    page.title = "NavigationBar con Validación por Vista"
    page.padding = 0
    page.spacing = 0

    # Snackbar con duración por defecto de 4 segundos
    snackbar = ft.SnackBar(
        content=ft.Text(""),
        bgcolor=ft.Colors.RED_500,
        duration=4000  # 4 segundos
    )
    page.snack_bar = snackbar

    def mostrar_snackbar(mensaje, color):
        snackbar.content = ft.Text(mensaje)
        snackbar.bgcolor = color
        snackbar.open = True
        page.update()

    # ----------- VISTA 1 ------------
    nombre = ft.TextField(label="Nombre")
    apellido = ft.TextField(label="Apellido")
    correo = ft.TextField(label="Correo")
    telefono = ft.TextField(label="Teléfono")

    def guardar_vista_1(e):
        if not all([nombre.value, apellido.value, correo.value, telefono.value]):
            mostrar_snackbar("Por favor, completa todos los campos.", ft.Colors.RED_500)
        else:
            mostrar_snackbar("Formulario guardado correctamente.", ft.Colors.GREEN_400)

    btn_guardar_1 = ft.FloatingActionButton(icon=ft.icons.SAVE, on_click=guardar_vista_1)

    vista_1 = ft.Stack([
        ft.Container(
            content=ft.Column([nombre, apellido, correo, telefono]),
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.Colors.BLUE_100,
        ),
        ft.Container(
            content=btn_guardar_1,
            alignment=ft.alignment.bottom_right,
            padding=20,
        )
    ])

    # ----------- VISTA 2 ------------
    checkboxes = [ft.Checkbox(label=f"Opción {chr(65 + i)}") for i in range(5)]

    def guardar_vista_2(e):
        if not any(cb.value for cb in checkboxes):
            mostrar_snackbar("Selecciona al menos una opción.", ft.Colors.RED_500)
        else:
            mostrar_snackbar("Opciones guardadas correctamente.", ft.Colors.GREEN_400)

    btn_guardar_2 = ft.FloatingActionButton(icon=ft.icons.SAVE_AS, on_click=guardar_vista_2)

    vista_2 = ft.Stack([
        ft.Container(
            content=ft.Column(checkboxes),
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.Colors.GREEN_100,
        ),
        ft.Container(
            content=btn_guardar_2,
            alignment=ft.alignment.bottom_right,
            padding=20,
        )
    ])

    # ----------- VISTA 3 ------------
    usuario = ft.TextField(label="Usuario")
    contraseña = ft.TextField(label="Contraseña", password=True)

    def guardar_vista_3(e):
        if not usuario.value or not contraseña.value:
            mostrar_snackbar("Usuario y contraseña requeridos.", ft.Colors.RED_500)
        else:
            mostrar_snackbar("Inicio de sesión guardado.", ft.Colors.GREEN_400)

    btn_guardar_3 = ft.FloatingActionButton(icon=ft.icons.CLOUD_UPLOAD, on_click=guardar_vista_3)

    vista_3 = ft.Stack([
        ft.Container(
            content=ft.Column([usuario, contraseña]),
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.Colors.AMBER_100,
        ),
        ft.Container(
            content=btn_guardar_3,
            alignment=ft.alignment.bottom_right,
            padding=20,
        )
    ])

    # ----------- CONTENEDOR Y NAVEGACIÓN ------------
    content_container = ft.Container(content=vista_1, expand=True)

    def on_nav_change(e):
        index = e.control.selected_index
        if index == 0:
            content_container.content = vista_1
        elif index == 1:
            content_container.content = vista_2
        elif index == 2:
            content_container.content = vista_3
        page.update()

    nav_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Formulario"),
            ft.NavigationBarDestination(icon=ft.icons.CHECK, label="Opciones"),
            ft.NavigationBarDestination(icon=ft.icons.LOGIN, label="Login"),
        ],
    )

    page.navigation_bar = nav_bar
    page.add(content_container)

ft.app(main)
