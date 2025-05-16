from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class AppStatus:
    is_connected: bool = False
    is_login: bool = False


@dataclass
class User:
    username: Optional[str] = "carlosmvp"
    password: Optional[str] = "sadfasdhfuyagsd~s"


@dataclass
class ConfigCntm(User):
    domain: Optional[str] = "uci.cu"
    proxy_server: Optional[str] = "10.0.0.1"
    proxy_port: Optional[int] = 8080
    no_proxy: List[str] = field(default_factory=lambda: ["*uci.cu", "127.00.1"])
    listen_port: Optional[int] = 3128
    listen_server: Optional[str] = "127.0.0.1"
    gateway: Optional[bool] = False


@dataclass
class DataSchema:
    app_status: AppStatus = field(default_factory=AppStatus)
    user: User = field(default_factory=User)
    config_cntm: ConfigCntm = field(default_factory=ConfigCntm)

@dataclass
class Cuota:
    total: Optional[float] = None
    used: Optional[float] = None
    remaining: Optional[float] = None
    active_time: Optional[str] = None
    
@dataclass
class configuracion_aviso_cuota:
    por_minuto: Optional[int] = None
    por_ciento: Optional[int] = None