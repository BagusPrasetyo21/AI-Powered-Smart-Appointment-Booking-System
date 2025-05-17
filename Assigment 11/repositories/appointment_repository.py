from typing import Optional, List
from datetime import datetime
from repositories.repository import Repository
from src.appointment import Appointment

class AppointmentRepository(Repository[Appointment, str]):
    """
    Repository interface for Appointment entities.
    Extends the generic Repository interface with Appointment-specific operations.
    """
    
    def find_by_patient_id(self, patient_id: str) -> List[Appointment]:
        """
        Find appointments by patient ID.
        
        Args:
            patient_id: The patient ID to search for
            
        Returns:
            A list of appointments for the specified patient
        """
        pass
    
    def find_by_doctor_id(self, doctor_id: str) -> List[Appointment]:
        """
        Find appointments by doctor ID.
        
        Args:
            doctor_id: The doctor ID to search for
            
        Returns:
            A list of appointments for the specified doctor
        """
        pass
    
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Appointment]:
        """
        Find appointments within a date range.
        
        Args:
            start_date: The start date of the range
            end_date: The end date of the range
            
        Returns:
            A list of appointments within the specified date range
        """
        pass
