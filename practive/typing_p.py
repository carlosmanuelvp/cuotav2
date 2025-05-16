import gi
gi.require_version('AyatanaAppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')
from gi.repository import AyatanaAppIndicator3 as AppIndicator
from gi.repository import Gtk
import signal

APP_ID = 'mi_aplicacion'

def on_conectar(widget):
    print("Conectando...")

def on_mostrar(widget):
    print("Mostrando...")

def on_salir(widget):
    Gtk.main_quit()

# Crear menú
menu = Gtk.Menu()

item_conectar = Gtk.MenuItem(label="Conectar")
item_conectar.connect("activate", on_conectar)
menu.append(item_conectar)

item_mostrar = Gtk.MenuItem(label="Mostrar")
item_mostrar.connect("activate", on_mostrar)
menu.append(item_mostrar)

item_salir = Gtk.MenuItem(label="Cerrar")
item_salir.connect("activate", on_salir)
menu.append(item_salir)

menu.show_all()

# Crear el indicador
indicator = AppIndicator.Indicator.new(
    APP_ID,
    "/usr/share/icons/gnome/32x32/status/dialog-information.png",  # Ícono
    AppIndicator.IndicatorCategory.APPLICATION_STATUS
)
indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
indicator.set_menu(menu)

# Mantener el proceso vivo
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
