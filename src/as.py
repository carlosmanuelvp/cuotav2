from plyer import notification

notification.notify(
    title='Conectado al proxy',
    message='La cuenta ha llegado al 80% de datos consumidos',
    app_icon='/assets/logouci.png',  # o .png dependiendo del sistema
    timeout=5
)
from plyer import notification

notification.notify(
    title='Conectado al proxy',
    message='La autenticación fue exitosa.',
    app_icon='/ruta/al/icono.ico',  # o .png dependiendo del sistema
    timeout=5
)
