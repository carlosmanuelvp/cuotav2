import gi
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')

from gi.repository import AppIndicator3, Gtk

def menuitem_response(menu_item, label):
    print(f"Seleccionaste: {label}")

def build_menu():
    menu = Gtk.Menu()

    item1 = Gtk.MenuItem(label='Opción 1')
    item1.connect('activate', menuitem_response, "Opción 1")
    menu.append(item1)

    item2 = Gtk.MenuItem(label='Opción 2')
    item2.connect('activate', menuitem_response, "Opción 2")
    menu.append(item2)

    item_quit = Gtk.MenuItem(label='Salir')
    item_quit.connect('activate', Gtk.main_quit)
    menu.append(item_quit)

    menu.show_all()
    return menu

def main():
    indicator = AppIndicator3.Indicator.new(
        "mi-icono",
        "dialog-information",  # Icono por defecto
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())

    Gtk.main()

if __name__ == "__main__":
    main()
