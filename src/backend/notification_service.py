from typing import Callable, Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class NotificationType(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    SUCCESS = "success"


@dataclass
class Notification:
    message: str
    type: NotificationType
    timestamp: datetime
    read: bool = False
    id: Optional[str] = None


class NotificationService:
    def __init__(self):
        self._notifications: List[Notification] = []
        self._subscribers: List[Callable] = []
        self._max_notifications = 50

    def subscribe(self, callback: Callable[[Notification], None]):
        """Suscribir una función para recibir notificaciones"""
        if callback not in self._subscribers:
            self._subscribers.append(callback)

    def unsubscribe(self, callback: Callable):
        """Desuscribir una función"""
        if callback in self._subscribers:
            self._subscribers.remove(callback)

    def notify(self, message: str, type: NotificationType = NotificationType.INFO):
        """Crear y enviar una nueva notificación"""
        notification = Notification(
            message=message, type=type, timestamp=datetime.now()
        )

        self._notifications.append(notification)

        # Mantener solo las últimas N notificaciones
        if len(self._notifications) > self._max_notifications:
            self._notifications = self._notifications[-self._max_notifications :]

        # Notificar a los suscriptores
        for subscriber in self._subscribers:
            try:
                subscriber(notification)
            except Exception:
                pass  # Ignorar errores en los callbacks

    def get_unread_notifications(self) -> List[Notification]:
        """Obtener notificaciones no leídas"""
        return [n for n in self._notifications if not n.read]

    def mark_as_read(self, notification_id: str):
        """Marcar una notificación como leída"""
        for notification in self._notifications:
            if notification.id == notification_id:
                notification.read = True
                break

    def clear_all(self):
        """Limpiar todas las notificaciones"""
        self._notifications.clear()

    def get_notification_stats(self) -> Dict:
        """Obtener estadísticas de notificaciones"""
        total = len(self._notifications)
        unread = len(self.get_unread_notifications())
        by_type = {
            t: len([n for n in self._notifications if n.type == t])
            for t in NotificationType
        }

        return {"total": total, "unread": unread, "by_type": by_type}
