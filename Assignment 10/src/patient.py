from datetime import date, datetime
from typing import List, Optional
from .contact_info import ContactInfo
from .enums import AppointmentType

class Patient:
    def __init__(self, patient_id: str, name: str, date_of_birth: date, 
                 medical_history_id: str, contact_info: ContactInfo):
        self._patient_id = patient_id
        self._name = name
        self._date_of_birth = date_of_birth
        self._medical_history_id = medical_history_id
        self._contact_info = contact_info
    
    @property
    def patient_id(self) -> str:
        return self._patient_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._contact_info.email
    
    @property
    def phone(self) -> str:
        return self._contact_info.phone
    
    @property
    def address(self) -> str:
        return self._contact_info.address
    
    @property
    def date_of_birth(self) -> date:
        return self._date_of_birth
    
    @property
    def medical_history_id(self) -> str:
        return self._medical_history_id
    
    @property
    def contact_info(self) -> ContactInfo:
        return self._contact_info
    
    def book_appointment(self, doctor_id: str, date_time: datetime, 
                         appointment_type: AppointmentType):
        """Book an appointment with a doctor"""
        # This would typically interact with an appointment service
        # For now, we'll return a placeholder
        from .appointment import Appointment
        import uuid
        
        appointment_id = str(uuid.uuid4())
        return Appointment(
            appointment_id=appointment_id,
            patient_id=self._patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            duration=30,  # Default duration in minutes
            appointment_type=appointment_type
        )
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an existing appointment"""
        # Implementation would interact with appointment service
        return True
    
    def reschedule_appointment(self, appointment_id: str, new_date_time: datetime):
        """Reschedule an existing appointment"""
        # Implementation would interact with appointment service
        from .appointment import Appointment
        # Placeholder return
        return Appointment(
            appointment_id=appointment_id,
            patient_id=self._patient_id,
            doctor_id="some-doctor-id",
            date_time=new_date_time,
            duration=30,
            appointment_type=AppointmentType.REGULAR
        )
    
    def rate_appointment(self, appointment_id: str, score: int, comment: str):
        """Rate a completed appointment"""
        from .rating import Rating
        import uuid
        
        rating_id = str(uuid.uuid4())
        return Rating(
            rating_id=rating_id,
            patient_id=self._patient_id,
            appointment_id=appointment_id,
            doctor_id="some-doctor-id",  # This would be retrieved from the appointment
            score=score,
            comment=comment
        )
    
    def sync_calendar(self, calendar_type: str) -> bool:
        """Sync appointments with external calendar"""
        # Implementation would interact with calendar service
        return True
    
    def view_appointment_history(self) -> List:
        """View history of all appointments"""
        # Implementation would retrieve from appointment service
        return []  # Placeholder empty list
