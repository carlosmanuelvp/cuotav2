# backend/state.py

from backend.models import AppStatus, User, ConfigCntm, ConfiguracionAvisoCuota

# Esta será la instancia global reutilizable en toda la app
app_data = AppStatus()
user_data = User()
proxy_conf = ConfigCntm()
cuota_aviso = ConfiguracionAvisoCuota()
