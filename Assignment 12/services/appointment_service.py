"""
Appointment service implementation for handling business logic related to appointments.
"""
from typing import List, Optional
from datetime import datetime, timedelta
from src.appointment import Appointment
from src.patient import Patient
from src.doctor import Doctor
from src.enums import AppointmentStatus
from repositories.appointment_repository import AppointmentRepository
from repositories.patient_repository import PatientRepository
from repositories.doctor_repository import DoctorRepository

class AppointmentService:
    """
    Service class for handling business logic related to appointments.
    """
    
    def __init__(
        self, 
        appointment_repository: AppointmentRepository,
        patient_repository: PatientRepository,
        doctor_repository: DoctorRepository
    ):
        """
        Initialize the appointment service with repositories.
        
        Args:
            appointment_repository: Repository for appointment data access
            patient_repository: Repository for patient data access
            doctor_repository: Repository for doctor data access
        """
        self.appointment_repository = appointment_repository
        self.patient_repository = patient_repository
        self.doctor_repository = doctor_repository
    
    def create_appointment(self, appointment: Appointment) -> Appointment:
        """
        Create a new appointment.
        
        Args:
            appointment: The appointment to create
            
        Returns:
            The created appointment
        
        Raises:
            ValueError: If validation fails
        """
        # Validate patient and doctor exist
        patient = self.patient_repository.find_by_id(appointment.patient.id)
        if not patient:
            raise ValueError(f"Patient with ID {appointment.patient.id} not found")
        
        doctor = self.doctor_repository.find_by_id(appointment.doctor.id)
        if not doctor:
            raise ValueError(f"Doctor with ID {appointment.doctor.id} not found")
        
        # Validate appointment time is in the future and at least 24 hours in advance
        now = datetime.now()
        if appointment.date_time < now:
            raise ValueError("Appointment time cannot be in the past")
        
        if appointment.date_time < now + timedelta(hours=24):
            raise ValueError("Appointments must be booked at least 24 hours in advance")
        
        # Check for doctor availability
        doctor_appointments = self.appointment_repository.find_by_doctor_id(doctor.id)
        for existing_appointment in doctor_appointments:
            # Skip cancelled appointments
            if existing_appointment.status == AppointmentStatus.CANCELLED:
                continue
                
            # Check for time overlap
            appointment_end_time = appointment.date_time + timedelta(minutes=appointment.duration)
            existing_end_time = existing_appointment.date_time + timedelta(minutes=existing_appointment.duration)
            
            if (appointment.date_time <= existing_appointment.date_time < appointment_end_time or
                appointment.date_time < existing_end_time <= appointment_end_time):
                raise ValueError(f"Doctor is already booked for this time slot")
        
        # Check patient appointment limit (max 3 per day)
        patient_appointments = self.appointment_repository.find_by_patient_id(patient.id)
        same_day_appointments = [
            a for a in patient_appointments 
            if a.date_time.date() == appointment.date_time.date() and 
            a.status != AppointmentStatus.CANCELLED
        ]
        
        if len(same_day_appointments) >= 3:
            raise ValueError("Patient cannot book more than 3 appointments in a single day")
        
        # Save the appointment
        self.appointment_repository.save(appointment)
        return appointment
    
    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        """
        Get an appointment by ID.
        
        Args:
            appointment_id: The ID of the appointment to get
            
        Returns:
            The appointment if found, None otherwise
        """
        return self.appointment_repository.find_by_id(appointment_id)
    
    def get_all_appointments(self) -> List[Appointment]:
        """
        Get all appointments.
        
        Returns:
            A list of all appointments
        """
        return self.appointment_repository.find_all()
    
    def update_appointment(self, appointment: Appointment) -> Appointment:
        """
        Update an existing appointment.
        
        Args:
            appointment: The appointment to update
            
        Returns:
            The updated appointment
            
        Raises:
            ValueError: If the appointment does not exist or validation fails
        """
        existing_appointment = self.appointment_repository.find_by_id(appointment.id)
        if not existing_appointment:
            raise ValueError(f"Appointment with ID {appointment.id} not found")
        
        # If date/time is being changed, validate the new time
        if appointment.date_time != existing_appointment.date_time:
            now = datetime.now()
            if appointment.date_time < now:
                raise ValueError("Appointment time cannot be in the past")
            
            if appointment.date_time < now + timedelta(hours=24):
                raise ValueError("Appointment changes must be made at least 24 hours in advance")
        
        # Save the updated appointment
        self.appointment_repository.save(appointment)
        return appointment
    
    def cancel_appointment(self, appointment_id: str) -> Appointment:
        """
        Cancel an appointment.
        
        Args:
            appointment_id: The ID of the appointment to cancel
            
        Returns:
            The cancelled appointment
            
        Raises:
            ValueError: If the appointment does not exist or cancellation is too late
        """
        appointment = self.appointment_repository.find_by_id(appointment_id)
        if not appointment:
            raise ValueError(f"Appointment with ID {appointment_id} not found")
        
        # Check if cancellation is at least 6 hours before the appointment
        now = datetime.now()
        if appointment.date_time < now + timedelta(hours=6):
            raise ValueError("Cancellations must be made at least 6 hours before the appointment")
        
        # Update status to cancelled
        appointment.status = AppointmentStatus.CANCELLED
        self.appointment_repository.save(appointment)
        return appointment
    
    def get_patient_appointments(self, patient_id: str) -> List[Appointment]:
        """
        Get all appointments for a patient.
        
        Args:
            patient_id: The ID of the patient
            
        Returns:
            A list of appointments for the patient
        """
        return self.appointment_repository.find_by_patient_id(patient_id)
    
    def get_doctor_appointments(self, doctor_id: str) -> List[Appointment]:
        """
        Get all appointments for a doctor.
        
        Args:
            doctor_id: The ID of the doctor
            
        Returns:
            A list of appointments for the doctor
        """
        return self.appointment_repository.find_by_doctor_id(doctor_id)
    
    def get_appointments_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Appointment]:
        """
        Get appointments within a date range.
        
        Args:
            start_date: The start date of the range
            end_date: The end date of the range
            
        Returns:
            A list of appointments within the date range
        """
        return self.appointment_repository.find_by_date_range(start_date, end_date)
