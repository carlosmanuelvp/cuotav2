from plyer import notification

notification.notify(
    title='AVISO',
    message='La cuenta ha llegado al 85% de datos consumidos',
  #  app_icon='/ruta/a/icono.ico',  # Usa .ico o .png (según el sistema)
    timeout=100  # Duración en segundos
)

