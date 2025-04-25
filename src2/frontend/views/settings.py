import flet as ft


def main(page: ft.Page):
    page.title = "NavigationBar con Contenidos Diferentes (Corregido)"
    # Alineación vertical START para que el contenido empiece arriba
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- 1. Definir los Contenedores para cada vista ---
    # Cada contenedor representa una "página" completa que se mostrará.
    # Usamos ft.Container para poder darle estilo y asegurar que ocupen espacio.

    vista_inicio = ft.Container(
        # Usamos Column para organizar el contenido dentro del contenedor
        content=ft.Column(
            [
                # CORREGIDO: ft.Icons y ft.Colors con mayúscula inicial
                ft.Icon(ft.Icons.HOME, size=150, color=ft.Colors.BLUE_ACCENT_700),
                ft.Text(
                    "Bienvenido a la Sección de Inicio",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Este es el contenido principal de la vista de inicio.",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            # Centrar los elementos de la columna horizontalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            # Espaciado entre elementos
            spacing=20,
        ),
        # Centrar la columna dentro del contenedor
        alignment=ft.alignment.center,
        # Ocupar todo el espacio vertical disponible sobre la barra de navegación
        expand=True,
        # Opcional: Color de fondo para ver claramente el cambio
        # bgcolor=ft.Colors.BLUE_GREY_50 # CORREGIDO: ft.Colors
    )

    vista_favoritos = ft.Container(
        content=ft.Column(
            [
                # CORREGIDO: ft.Icons y ft.Colors con mayúscula inicial
                ft.Icon(ft.Icons.FAVORITE, size=150, color=ft.Colors.PINK_ACCENT_700),
                ft.Text(
                    "Sección de Favoritos",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Aquí verías tus elementos guardados como favoritos.",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Checkbox(label="Elemento favorito 1"),
                ft.Checkbox(label="Elemento favorito 2"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
        # bgcolor=ft.Colors.PINK_50 # CORREGIDO: ft.Colors
    )

    vista_perfil = ft.Container(
        content=ft.Column(
            [
                # CORREGIDO: ft.Icons y ft.Colors con mayúscula inicial
                ft.Icon(ft.Icons.PERSON, size=150, color=ft.Colors.GREEN_ACCENT_700),
                ft.Text(
                    "Tu Perfil",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.TextField(
                    label="Nombre de usuario", value="Usuario Flet", read_only=True
                ),
                ft.ElevatedButton("Editar Perfil (simulado)"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
        # bgcolor=ft.Colors.GREEN_50 # CORREGIDO: ft.Colors
    )

    # --- Guardamos las vistas en una lista para fácil acceso por índice ---
    # ¡El orden aquí DEBE COINCIDIR con el orden de los NavigationBarDestination!
    todas_las_vistas = [vista_inicio, vista_favoritos, vista_perfil]

    # --- 2. Función que se llama cuando cambia la selección ---
    def cambiar_vista(e):
        # e.data contiene el índice (como string) del destino seleccionado
        indice_seleccionado = int(e.data)
        print(f"Navegando al índice: {indice_seleccionado}")  # Útil para depurar

        # Limpiar TODO el contenido actual de la página principal
        page.controls.clear()

        # Añadir el contenedor/vista correspondiente al índice seleccionado
        page.add(todas_las_vistas[indice_seleccionado])

        # Muy importante: Actualizar la página para que se muestren los cambios
        page.update()

    # --- 3. Crear y asignar la NavigationBar ---
    page.navigation_bar = ft.NavigationBar(
        # Definir los destinos (botones/pestañas)
        destinations=[
            # CORREGIDO: Usar ft.NavigationBarDestination y ft.Icons
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,  # Icono normal
                selected_icon=ft.Icons.HOME,  # Icono cuando está seleccionado
                label="Inicio",  # Texto debajo del icono
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="Favoritos",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINE,
                selected_icon=ft.Icons.PERSON,
                label="Perfil",
            ),
        ],
        # Índice del destino que estará seleccionado al inicio (0 es el primero)
        selected_index=1,
        # Función a ejecutar cuando el usuario selecciona un destino diferente
        on_change=cambiar_vista,
    )

    # --- 4. Mostrar la vista inicial ---
    # Al arrancar la app, mostramos el contenido correspondiente al selected_index (0)
    page.add(todas_las_vistas[0])

    # Flet llamará a page.update() implícitamente aquí al final de la función main,
    # pero en la función cambiar_vista SÍ necesitamos llamarlo explícitamente.


# Ejecutar la aplicación
ft.app(target=main)
