from datetime import datetime
from .enums import NotificationType, NotificationStatus, RecipientType

class Notification:
    def __init__(self, notification_id: str, recipient_id: str, recipient_type: RecipientType,
                 type: NotificationType, content: str, appointment_id: str,
                 status: NotificationStatus = NotificationStatus.PENDING):
        self._notification_id = notification_id
        self._recipient_id = recipient_id
        self._recipient_type = recipient_type
        self._type = type
        self._content = content
        self._timestamp = datetime.now()
        self._status = status
        self._appointment_id = appointment_id
    
    @property
    def notification_id(self) -> str:
        return self._notification_id
    
    @property
    def recipient_id(self) -> str:
        return self._recipient_id
    
    @property
    def recipient_type(self) -> RecipientType:
        return self._recipient_type
    
    @property
    def type(self) -> NotificationType:
        return self._type
    
    @property
    def content(self) -> str:
        return self._content
    
    @property
    def timestamp(self) -> datetime:
        return self._timestamp
    
    @property
    def status(self) -> NotificationStatus:
        return self._status
    
    @property
    def appointment_id(self) -> str:
        return self._appointment_id
    
    def send(self) -> bool:
        """Send the notification"""
        if self._status == NotificationStatus.PENDING:
            # In a real system, this would use a notification service
            self._status = NotificationStatus.SENT
            return True
        return False
    
    def mark_as_read(self) -> bool:
        """Mark the notification as read"""
        if self._status in [NotificationStatus.SENT, NotificationStatus.DELIVERED]:
            self._status = NotificationStatus.READ
            return True
        return False
    
    def mark_as_delivered(self) -> bool:
        """Mark the notification as delivered"""
        if self._status == NotificationStatus.SENT:
            self._status = NotificationStatus.DELIVERED
            return True
        return False
    
    def resend(self) -> bool:
        """Resend a failed notification"""
        if self._status == NotificationStatus.FAILED:
            self._status = NotificationStatus.PENDING
            return self.send()
        return False
