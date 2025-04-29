import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Apps"
    page.vertical_alignment = ft.MainAxisAlignment.START
    # Ajusta el tamaño inicial de la ventana si lo deseas
    page.window_width = 350
    page.window_height = 500

    # --- Datos de ejemplo para las aplicaciones ---
    # Puedes reemplazar esto con tus propios datos.
    # ft.icons.APPS es un icono genérico, puedes usar otros o cargar imágenes.
    apps_info = [
        {"name": "Github Desktop", "icon": ft.icons.COMPUTER}, # Usando un icono de ejemplo
        {"name": "Github Desktop", "icon": ft.icons.COMPUTER},
        {"name": "Github Desktop", "icon": ft.icons.COMPUTER},
        {"name": "Otra App", "icon": ft.icons.APPS},
        {"name": "Ajustes", "icon": ft.icons.SETTINGS},
        {"name": "Navegador Web", "icon": ft.icons.WEB},
        {"name": "Editor de Texto", "icon": ft.icons.EDIT},
        {"name": "Calculadora", "icon": ft.icons.CALCULATE},
        {"name": "Visor de Imágenes", "icon": ft.icons.IMAGE},
        {"name": "Reproductor", "icon": ft.icons.PLAY_CIRCLE_FILL},
        {"name": "Terminal", "icon": ft.icons.TERMINAL},
    ] * 2 # Multiplicamos para tener más elementos y probar el scroll

    # --- Columna principal que contendrá las filas de las apps ---
    # Es importante 'expand=True' para que el scroll funcione correctamente dentro del espacio asignado
    apps_list_column = ft.Column(
        scroll=ft.ScrollMode.ADAPTIVE, # Habilita el scroll si el contenido excede el tamaño
        expand=True,
        spacing=5 # Espacio vertical entre elementos
    )

    # --- Función para eliminar una app de la lista ---
    def remove_app(e):
        # 'e.control' es el IconButton que se presionó.
        # 'e.control.data' contiene la fila (Row) que le asignamos.
        row_to_remove = e.control.data
        apps_list_column.controls.remove(row_to_remove) # Elimina el control de la columna
        page.update() # Actualiza la interfaz para reflejar el cambio

    # --- Función para crear una fila (Row) para una app ---
    def create_app_row(app_data):
        # Creamos la fila (Row) primero para poder referenciarla en el botón
        app_row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # Alinea elementos (icono/texto a la izq, botón a la der)
            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centra verticalmente los elementos en la fila
        )

        # Creamos los controles para esta fila
        app_row.controls = [
            # Icono de la app
            ft.Icon(name=app_data["icon"], color=ft.colors.BLUE_GREY),
            # Nombre de la app (expand=True para que ocupe el espacio disponible)
            ft.Text(app_data["name"], expand=True, color=ft.colors.BLUE_GREY_700),
            # Botón para eliminar (X)
            ft.IconButton(
                icon=ft.icons.CLOSE, # Icono de 'X'
                icon_color=ft.colors.RED_400, # Color del icono 'X'
                tooltip="Quitar", # Texto que aparece al pasar el ratón por encima
                on_click=remove_app, # Función que se llama al hacer clic
                data=app_row # ¡Importante! Guardamos la referencia a esta fila en el botón
            )
        ]
        return app_row

    # --- Llenar la columna con las filas de las apps ---
    for app_data in apps_info:
        apps_list_column.controls.append(create_app_row(app_data))

    # --- Añadir los controles principales a la página ---
    page.add(
        ft.Container( # Un contenedor para darle un poco de padding y estructura
            padding=10,
            # border=ft.border.all(1, ft.colors.OUTLINE), # Borde opcional como en la imagen
            # border_radius=ft.border_radius.all(5), # Esquinas redondeadas opcionales
            content=ft.Column( # Columna para el título y la lista
                [
                    ft.Text("Apps", style=ft.TextThemeStyle.HEADLINE_MEDIUM, text_align=ft.TextAlign.CENTER),
                    ft.Divider(height=1, color=ft.colors.BLUE_GREY_100), # Línea separadora
                    apps_list_column, # La columna desplazable con las apps
                ],
                expand=True # Permite que esta columna interna se expanda
            ),
            expand=True # Permite que el contenedor principal se expanda
        )
    )

    page.update() # Dibuja la interfaz inicial

# --- Ejecutar la aplicación Flet ---
# Asegúrate de tener flet instalado: pip install flet==0.27.0 (o la versión específica que necesites)
ft.app(target=main)
