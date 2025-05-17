from datetime import datetime
from typing import List, Optional
from .contact_info import ContactInfo

class Doctor:
    def __init__(self, doctor_id: str, name: str, specialization: str, 
                 department: str, license_number: str, contact_info: ContactInfo):
        self._doctor_id = doctor_id
        self._name = name
        self._specialization = specialization
        self._department = department
        self._license_number = license_number
        self._contact_info = contact_info
    
    @property
    def doctor_id(self) -> str:
        return self._doctor_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def specialization(self) -> str:
        return self._specialization
    
    @property
    def email(self) -> str:
        return self._contact_info.email
    
    @property
    def phone(self) -> str:
        return self._contact_info.phone
    
    @property
    def department(self) -> str:
        return self._department
    
    @property
    def license_number(self) -> str:
        return self._license_number
    
    @property
    def contact_info(self) -> ContactInfo:
        return self._contact_info
    
    def set_availability(self, working_hours, blocked_slots) -> bool:
        """Set doctor's availability"""
        # This would typically interact with a schedule service
        # For now, we'll return a placeholder
        return True
    
    def view_appointments(self, date_range) -> List:
        """View appointments within a date range"""
        # Implementation would retrieve from appointment service
        return []  # Placeholder empty list
    
    def update_schedule(self, schedule_changes) -> bool:
        """Update doctor's schedule with changes"""
        # Implementation would interact with schedule service
        return True
    
    def access_patient_history(self, patient_id: str):
        """Access a patient's medical record"""
        from .medical_record import MedicalRecord
        # This would typically retrieve the actual record from a database
        # For now, we'll return a placeholder
        return MedicalRecord(
            record_id="placeholder-record-id",
            patient_id=patient_id,
            diagnoses=[],
            medications=[],
            allergies=[],
            notes="",
            last_updated=datetime.now()
        )
    
    def sync_calendar(self, calendar_type: str) -> bool:
        """Sync schedule with external calendar"""
        # Implementation would interact with calendar service
        return True
