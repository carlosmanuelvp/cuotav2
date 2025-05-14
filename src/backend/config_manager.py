import json
import os
from typing import Dict, Any


class ConfigManager:
    def __init__(self, config_file: str = "settings.json"):
        self.config_file = config_file
        self.config_data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Carga la configuración desde el archivo JSON"""
        if not os.path.exists(self.config_file):
            return self._create_default_config()

        try:
            with open(self.config_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return self._create_default_config()

    def _create_default_config(self) -> Dict[str, Any]:
        """Crea una configuración por defecto"""
        default_config = {
            "cntlm": {
                "enabled": False,
                "username": "",
                "domain": "",
                "proxy": "",
                "port": 3128,
            },
            "network": {"check_interval": 30, "speed_test_interval": 3600},
            "ui": {"theme": "light", "language": "es"},
        }
        self.save_config(default_config)
        return default_config

    def save_config(self, config: Dict[str, Any]) -> None:
        """Guarda la configuración en el archivo JSON"""
        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=4)
        self.config_data = config

    def get_config(self, key: str = None) -> Any:
        """Obtiene un valor específico o toda la configuración"""
        if key is None:
            return self.config_data
        return self.config_data.get(key)

    def update_config(self, key: str, value: Any) -> None:
        """Actualiza un valor específico en la configuración"""
        keys = key.split(".")
        current = self.config_data

        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        current[keys[-1]] = value
        self.save_config(self.config_data)
