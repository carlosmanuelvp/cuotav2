import flet as ft

# Vista de inicio de sesión
def login_view(page: ft.Page, on_login_success):
    # Fondo degradado mejorado (blanco a tonos de azul claro con más profundidad)
    gradient_background = ft.Container(
        width=page.window_width,
        height=page.windowheight,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),  # Desde la esquina superior izquierda
            end=ft.Alignment(1, 1),      # Hasta la esquina inferior derecha
            colors=[
                ft.Colors.WHITE,          # Blanco puro
                ft.Colors.LIGHT_BLUE_50,  # Azul muy claro
                ft.Colors.LIGHT_BLUE_100, # Azul claro
                ft.Colors.LIGHT_BLUE_200  # Azul un poco más intenso
            ],
            rotation=1.2  # Ajuste de rotación para un efecto de ondas más natural
        )
    )

    # Capa adicional para simular ondas (con opacidad)
    wave_effect = ft.Container(
        width=page.window_width,
        height=page.window_height,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, 0),  # Desde la izquierda
            end=ft.Alignment(1, 0),     # Hasta la derecha
            colors=[
                ft.Colors.TRANSPARENT,
                ft.Colors.LIGHT_BLUE_50.with_opacity(0.3),  # Azul claro con opacidad
                ft.Colors.TRANSPARENT
            ],
            rotation=0.5  # Rotación diferente para crear un efecto de onda
        )
    )

    # Campos de entrada
    username_field = ft.TextField(
        label="Usuario",
        width=300,
        border_radius=10,
        bgcolor="#E6FFFFFF",  # Blanco con opacidad 0.9
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
    )

    password_field = ft.TextField(
        label="Contraseña",
        password=True,
        width=300,
        border_radius=10,
        bgcolor="#E6FFFFFF",  # Blanco con opacidad 0.9
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
    )

    # Mensaje de error (inicialmente vacío)
    error_message = ft.Text("", color=ft.Colors.RED, size=16)

    # Función para validar el login
    def validate_login(e):
        username = username_field.value
        password = password_field.value

        # Validación simple (puedes cambiar esto por una base de datos o API)
        if username == "admin" and password == "1234":
            on_login_success()  # Llama a la función para cambiar de vista
        else:
            error_message.value = "Usuario o contraseña incorrectos"
            page.update()

    # Botón de inicio de sesión
    login_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        width=300,
        height=50,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        on_click=validate_login
    )

    # Contenido de la vista de login
    content = ft.Column(
        controls=[
            ft.Text(
                "Inicio de Sesión",
                size=30,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            username_field,
            password_field,
            error_message,
            login_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Superponemos el fondo degradado y el efecto de ondas
    return ft.Stack(controls=[gradient_background, wave_effect, content])

# Vista de bienvenida (después del login)
def welcome_view(page: ft.Page, on_logout):
    # Fondo degradado mejorado (blanco a tonos de azul claro con más profundidad)
    gradient_background = ft.Container(
        width=page.window.width,
        height=page.window.height,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                ft.Colors.WHITE,
                ft.Colors.LIGHT_BLUE_50,
                ft.Colors.LIGHT_BLUE_100,
                ft.Colors.LIGHT_BLUE_200
            ],
            rotation=1.2
        )
    )

    # Capa adicional para simular ondas (con opacidad)
    wave_effect = ft.Container(
        width=page.window_width,
        height=page.window_height,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, 0),
            end=ft.Alignment(1, 0),
            colors=[
                ft.Colors.TRANSPARENT,
                ft.Colors.LIGHT_BLUE_50.with_opacity(0.3),
                ft.Colors.TRANSPARENT
            ],
            rotation=0.5
        )
    )

    # Botón de cerrar sesión
    logout_button = ft.ElevatedButton(
        text="Cerrar Sesión",
        width=300,
        height=50,
        bgcolor=ft.Colors.RED_700,
        color=ft.Colors.WHITE,
        on_click=lambda e: on_logout()
    )

    # Contenido de la vista de bienvenida
    content = ft.Column(
        controls=[
            ft.Text(
                "¡Bienvenido!",
                size=30,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            logout_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Superponemos el fondo degradado y el efecto de ondas
    return ft.Stack(controls=[gradient_background, wave_effect, content])

# Función principal
def main(page: ft.Page):
    # Configuración básica de la ventana
    page.title = "Sistema de Login"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False
    page.padding = 0
    page.bgcolor = ft.Colors.TRANSPARENT

    # Función para mostrar la vista de login
    def show_login():
        page.controls.clear()  # Limpia la pantalla actual
        page.add(login_view(page, show_welcome))  # Muestra la vista de login
        page.update()

    # Función para mostrar la vista de bienvenida
    def show_welcome():
        page.controls.clear()  # Limpia la pantalla actual
        page.add(welcome_view(page, show_login))  # Muestra la vista de bienvenida
        page.update()

    # Inicia mostrando la vista de login
    show_login()

# Ejecutar la aplicación
ft.app(target=main)
