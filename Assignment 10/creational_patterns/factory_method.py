from abc import ABC, abstractmethod
import uuid
import sys
import os
from datetime import datetime

# Add the parent directory to the path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.notification import Notification
from src.enums import NotificationType, NotificationStatus, RecipientType

class NotificationSender(ABC):
    """
    Factory Method Pattern: Abstract Creator
    
    This abstract class defines the factory method for creating notifications
    but lets subclasses decide which class to instantiate.
    """
    
    @abstractmethod
    def create_notification(self, recipient_id: str, content: str, appointment_id: str) -> Notification:
        """Factory method to be implemented by subclasses"""
        pass
    
    def send_notification(self, recipient_id: str, content: str, appointment_id: str) -> bool:
        """
        Template method that uses the factory method
        """
        notification = self.create_notification(recipient_id, content, appointment_id)
        return notification.send()


class EmailNotificationSender(NotificationSender):
    """Concrete Creator for Email Notifications"""
    
    def create_notification(self, recipient_id: str, content: str, appointment_id: str) -> Notification:
        notification_id = str(uuid.uuid4())
        email_content = f"EMAIL: {content}"
        
        return Notification(
            notification_id=notification_id,
            recipient_id=recipient_id,
            recipient_type=RecipientType.PATIENT,  # Default, could be parameterized
            type=NotificationType.GENERAL,  # Default, could be parameterized
            content=email_content,
            appointment_id=appointment_id,
            status=NotificationStatus.PENDING
        )


class SMSNotificationSender(NotificationSender):
    """Concrete Creator for SMS Notifications"""
    
    def create_notification(self, recipient_id: str, content: str, appointment_id: str) -> Notification:
        notification_id = str(uuid.uuid4())
        sms_content = f"SMS: {content}"
        
        return Notification(
            notification_id=notification_id,
            recipient_id=recipient_id,
            recipient_type=RecipientType.PATIENT,  # Default, could be parameterized
            type=NotificationType.GENERAL,  # Default, could be parameterized
            content=sms_content,
            appointment_id=appointment_id,
            status=NotificationStatus.PENDING
        )


class PushNotificationSender(NotificationSender):
    """Concrete Creator for Push Notifications"""
    
    def create_notification(self, recipient_id: str, content: str, appointment_id: str) -> Notification:
        notification_id = str(uuid.uuid4())
        push_content = f"PUSH: {content}"
        
        return Notification(
            notification_id=notification_id,
            recipient_id=recipient_id,
            recipient_type=RecipientType.PATIENT,  # Default, could be parameterized
            type=NotificationType.GENERAL,  # Default, could be parameterized
            content=push_content,
            appointment_id=appointment_id,
            status=NotificationStatus.PENDING
        )
