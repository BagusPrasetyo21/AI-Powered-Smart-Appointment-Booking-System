from typing import List
from datetime import datetime
from repositories.inmemory.base_inmemory_repository import BaseInMemoryRepository
from repositories.appointment_repository import AppointmentRepository
from src.appointment import Appointment

class InMemoryAppointmentRepository(BaseInMemoryRepository[Appointment, str], AppointmentRepository):
    """
    In-memory implementation of the AppointmentRepository interface.
    """
    
    def _get_entity_id(self, entity: Appointment) -> str:
        """Get the ID of an appointment entity."""
        return entity.appointment_id
    
    def find_by_patient_id(self, patient_id: str) -> List[Appointment]:
        """
        Find appointments by patient ID.
        
        Args:
            patient_id: The patient ID to search for
            
        Returns:
            A list of appointments for the specified patient
        """
        return [
            appointment for appointment in self._storage.values()
            if appointment.patient_id == patient_id
        ]
    
    def find_by_doctor_id(self, doctor_id: str) -> List[Appointment]:
        """
        Find appointments by doctor ID.
        
        Args:
            doctor_id: The doctor ID to search for
            
        Returns:
            A list of appointments for the specified doctor
        """
        return [
            appointment for appointment in self._storage.values()
            if appointment.doctor_id == doctor_id
        ]
    
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Appointment]:
        """
        Find appointments within a date range.
        
        Args:
            start_date: The start date of the range
            end_date: The end date of the range
            
        Returns:
            A list of appointments within the specified date range
        """
        return [
            appointment for appointment in self._storage.values()
            if start_date <= appointment.date_time <= end_date
        ]
