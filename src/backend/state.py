# backend/state.py

from backend.models import AppStatus , User

# Esta será la instancia global reutilizable en toda la app
app_data = AppStatus()
user_data = User()