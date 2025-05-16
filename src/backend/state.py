# backend/state.py

from backend.models import AppStatus , User, ConfigCntm, configuracion_aviso_cuota

# Esta será la instancia global reutilizable en toda la app
app_data = AppStatus()
user_data = User()
proxy_conf= ConfigCntm()
cuota_aviso = configuracion_aviso_cuota()
