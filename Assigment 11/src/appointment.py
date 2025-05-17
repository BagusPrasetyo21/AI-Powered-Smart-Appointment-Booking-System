from datetime import datetime
from typing import Optional
from .enums import AppointmentStatus, AppointmentType, NotificationType

class Appointment:
    def __init__(self, appointment_id: str, patient_id: str, doctor_id: str,
                 date_time: datetime, duration: int, 
                 appointment_type: AppointmentType,
                 status: AppointmentStatus = AppointmentStatus.SCHEDULED,
                 notes: str = ""):
        self._appointment_id = appointment_id
        self._patient_id = patient_id
        self._doctor_id = doctor_id
        self._date_time = date_time
        self._duration = duration
        self._status = status
        self._type = appointment_type
        self._notes = notes
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
    
    @property
    def appointment_id(self) -> str:
        return self._appointment_id
    
    @property
    def patient_id(self) -> str:
        return self._patient_id
    
    @property
    def doctor_id(self) -> str:
        return self._doctor_id
    
    @property
    def date_time(self) -> datetime:
        return self._date_time
    
    @property
    def duration(self) -> int:
        return self._duration
    
    @property
    def status(self) -> AppointmentStatus:
        return self._status
    
    @property
    def type(self) -> AppointmentType:
        return self._type
    
    @property
    def notes(self) -> str:
        return self._notes
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @property
    def updated_at(self) -> datetime:
        return self._updated_at
    
    def confirm(self) -> bool:
        """Confirm the appointment"""
        if self._status == AppointmentStatus.SCHEDULED:
            self._status = AppointmentStatus.CONFIRMED
            self._updated_at = datetime.now()
            return True
        return False
    
    def cancel(self, reason: str) -> bool:
        """Cancel the appointment with a reason"""
        if self._status not in [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED, AppointmentStatus.NO_SHOW]:
            self._status = AppointmentStatus.CANCELLED
            self._notes += f"\nCancellation reason: {reason}"
            self._updated_at = datetime.now()
            return True
        return False
    
    def reschedule(self, new_date_time: datetime) -> bool:
        """Reschedule the appointment to a new date and time"""
        if self._status not in [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED, AppointmentStatus.NO_SHOW]:
            self._date_time = new_date_time
            self._updated_at = datetime.now()
            return True
        return False
    
    def send_reminder(self):
        """Send a reminder notification for this appointment"""
        return self.generate_notification(NotificationType.REMINDER)
    
    def generate_notification(self, notification_type: NotificationType):
        """Generate a notification of the specified type"""
        from .notification import Notification
        import uuid
        
        notification_id = str(uuid.uuid4())
        
        # Content would be generated based on notification type and appointment details
        content = f"{notification_type.name} for appointment on {self._date_time}"
        
        # For simplicity, we'll send to the patient
        from .enums import RecipientType
        
        return Notification(
            notification_id=notification_id,
            recipient_id=self._patient_id,
            recipient_type=RecipientType.PATIENT,
            type=notification_type,
            content=content,
            appointment_id=self._appointment_id
        )
