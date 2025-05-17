from datetime import datetime
import uuid
import sys
import os

# Add the parent directory to the path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.appointment import Appointment
from src.enums import AppointmentType, AppointmentStatus

class AppointmentFactory:
    """
    Simple Factory Pattern Implementation
    
    This factory centralizes the creation of different types of appointments,
    hiding the instantiation logic from the client.
    """
    
    @staticmethod
    def create_appointment(patient_id: str, doctor_id: str, date_time: datetime, 
                          appointment_type: AppointmentType, notes: str = "") -> Appointment:
        """
        Create an appointment of the specified type
        """
        appointment_id = str(uuid.uuid4())
        
        # Default duration based on appointment type
        duration_map = {
            AppointmentType.REGULAR: 30,
            AppointmentType.FOLLOW_UP: 20,
            AppointmentType.EMERGENCY: 60,
            AppointmentType.CONSULTATION: 45,
            AppointmentType.PROCEDURE: 90
        }
        
        duration = duration_map.get(appointment_type, 30)
        
        return Appointment(
            appointment_id=appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            duration=duration,
            appointment_type=appointment_type,
            status=AppointmentStatus.SCHEDULED,
            notes=notes
        )
    
    @staticmethod
    def create_regular_appointment(patient_id: str, doctor_id: str, date_time: datetime) -> Appointment:
        """Convenience method to create a regular appointment"""
        return AppointmentFactory.create_appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            appointment_type=AppointmentType.REGULAR
        )
    
    @staticmethod
    def create_follow_up_appointment(patient_id: str, doctor_id: str, date_time: datetime) -> Appointment:
        """Convenience method to create a follow-up appointment"""
        return AppointmentFactory.create_appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            appointment_type=AppointmentType.FOLLOW_UP
        )
    
    @staticmethod
    def create_emergency_appointment(patient_id: str, doctor_id: str, date_time: datetime) -> Appointment:
        """Convenience method to create an emergency appointment"""
        return AppointmentFactory.create_appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            appointment_type=AppointmentType.EMERGENCY,
            notes="EMERGENCY: Requires immediate attention"
        )
