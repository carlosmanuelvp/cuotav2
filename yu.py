import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, AppIndicator3
import signal

def conectar(_):
    print("Conectando...")

def mostrar(_):
    print("Mostrando ventana...")

def salir(_):
    Gtk.main_quit()

def main():
    icono_path = "/ruta/absoluta/a/tu/icono.png"  # Cambia aquí por el path real

    indicator = AppIndicator3.Indicator.new(
        "mi_app_indicator",
        icono_path,
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    menu = Gtk.Menu()

    opciones = [
        ("Conectar", conectar),
        ("Mostrar", mostrar),
        ("Salir", salir)
    ]

    for texto, callback in opciones:
        item = Gtk.MenuItem(label=texto)
        item.connect("activate", callback)
        menu.append(item)

    menu.show_all()
    indicator.set_menu(menu)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()

if __name__ == "__main__":
    main()
