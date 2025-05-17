import flet as ft
import pystray
from PIL import Image, ImageDraw
import threading
import sys
import os


# --- Crear icono dinámico ---
def create_image():
    # Imagen simple con texto
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), color=(0, 155, 255))
    dc = ImageDraw.Draw(image)
    dc.text((width // 2, height // 2), "F", fill=(255, 255, 255), anchor="mm")
    return image


# --- Acciones del menú del icono ---
def on_open_app(icon, item):
    print("Abrir ventana principal")
    # Aquí puedes reabrir tu ventana si la minimizaste

def on_exit(icon, item):
    print("Saliendo...")
    icon.stop()
    os._exit(0)


# --- Iniciar el icono del sistema ---
def setup_system_tray():
    icon = pystray.Icon("flet-app", create_image(), "Mi App Flet", menu=pystray.Menu(
        pystray.MenuItem("Abrir App", on_open_app),
        pystray.MenuItem("Salir", on_exit)
    ))
    icon.run()


# --- Lanzar Flet en hilo separado ---
def run_flet_app(page: ft.Page):
    page.title = "App Flet con System Tray"
    page.add(ft.Text("Hola desde Flet!", size=30))


# --- Iniciar ambos componentes ---
def main():
    # Iniciar icono del sistema en hilo separado
    tray_thread = threading.Thread(target=setup_system_tray, daemon=True)
    tray_thread.start()

    # Iniciar Flet
    ft.app(target=run_flet_app)


if __name__ == "__main__":
    main()
