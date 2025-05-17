import flet as ft

def main(page: ft.Page):
    page.title = "Proxy App - Mejorado"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Opcional: Define un tema simple
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE_ACCENT_700, # Un color base para el tema
        # Puedes añadir más personalizaciones aquí
    )

    # Elementos de la UI
    logo = ft.Image(
        src="/src/assets/logoci.png", # Reemplaza con la URL o ruta local de tu logo
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )

    title = ft.Text(
        "Universidad de las Ciencias Informáticas",
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    subtitle = ft.Text(
        "Proxy App",
        size=16,
        color=ft.colors.BLACK54,
        text_align=ft.TextAlign.CENTER,
    )

    username_field = ft.TextField(
        label="Usuario",
        prefix_icon=ft.icons.PERSON,
        border=ft.InputBorder.OUTLINE, # Borde delineado moderno
        width=300,
        bgcolor=ft.colors.WHITE, # Fondo blanco para el campo
    )

    password_field = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.icons.LOCK,
        suffix_icon=ft.icons.VISIBILITY, # Icono para mostrar/ocultar contraseña
        password=True, # Para ocultar la contraseña
        can_reveal_password=True, # Permitir mostrar/ocultar
        border=ft.InputBorder.OUTLINE,
        width=300,
        bgcolor=ft.colors.WHITE,
    )

    remember_me_checkbox = ft.Checkbox(label="Mantener sesión iniciada")

    login_button = ft.ElevatedButton(
            "Iniciar Sesión",
            on_click=lambda e: print("Login button clicked"), # Reemplaza con tu lógica de login
            width=300,
            height=45,
            # Cambia esta línea:
            bgcolor=ft.colors.BLUE_ACCENT_700, # Usamos directamente el color deseado o similar a la semilla
            # O podrías usar un azul estándar como:
            # bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE, # Color del texto del botón
            elevation=5, # Sombra para darle profundidad
        )

    # Estructura del Layout
    layout = ft.Container(
        content=ft.Column(
            [
                logo,
                ft.Container(height=10), # Espacio
                title,
                 ft.Container(height=5), # Espacio
                subtitle,
                ft.Container(height=30), # Espacio
                username_field,
                ft.Container(height=15), # Espacio
                password_field,
                remember_me_checkbox,
                ft.Container(height=20), # Espacio
                login_button,
            ],
            spacing=0, # Controlado por los ft.Container(height=...)
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=400, # Ancho máximo del formulario
        padding=ft.padding.all(30),
        border_radius=ft.border_radius.all(15), # Bordes redondeados
        bgcolor=ft.colors.WHITE, # Fondo blanco para el contenedor principal del formulario
        # Opcional: añadir sombra al contenedor
        # shadow=ft.BoxShadow(
        #     spread_radius=1,
        #     blur_radius=10,
        #     color=ft.colors.BLACK26,
        #     offset=ft.Offset(0, 0),
        # ),
    )

    # Añadir el layout a la página
    page.add(layout)

# Para ejecutar la app (en modo escritorio)
if __name__ == "__main__":
    ft.app(target=main)

# Para ejecutar la app en modo web (cambia el view)
# if __name__ == "__main__":
#     ft.app(target=main, view=ft.AppView.WEB_BROWSER)
