from dataclasses import dataclass, field,
from typing import Optional


@dataclass
class AppContext:
    user: Optional[str] = field(default=None)
    password: Optional[str] = field(default=None)
    is_connected: bool = field(default=False)

    def change_connection(self):
        self.is_connected = not self.is_connected
