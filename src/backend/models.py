from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class AppStatus:
    is_connected: bool = False
    is_login: bool = True


@dataclass
class User:
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass
class ConfigCntm(User):
    domain: Optional[str] = "uci.cu"
    proxy_server: Optional[str] = "10.0.0.1"
    proxy_port: Optional[int] = 8080
    no_proxy: List[str] = field(default_factory=lambda: ["*uci.cu", "127.00.1"])
    listen_port: Optional[int] = 345435
    gateway: Optional[bool] = False


@dataclass
class DataSchema:
    app_status: AppStatus = field(default_factory=AppStatus)
    user: User = field(default_factory=User)
    config_cntm: ConfigCntm = field(default_factory=ConfigCntm)
