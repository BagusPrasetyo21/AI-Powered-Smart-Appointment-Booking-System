"""
Unit tests for the appointment service.
"""
import unittest
from unittest.mock import Mock, MagicMock
from datetime import datetime, timedelta
from src.appointment import Appointment
from src.patient import Patient
from src.doctor import Doctor
from src.enums import AppointmentStatus
from repositories.appointment_repository import AppointmentRepository
from repositories.patient_repository import PatientRepository
from repositories.doctor_repository import DoctorRepository
from services.appointment_service import AppointmentService

class TestAppointmentService(unittest.TestCase):
    """
    Test cases for the appointment service.
    """
    
    def setUp(self):
        """Set up test fixtures."""
        self.appointment_repository = Mock(spec=AppointmentRepository)
        self.patient_repository = Mock(spec=PatientRepository)
        self.doctor_repository = Mock(spec=DoctorRepository)
        
        self.appointment_service = AppointmentService(
            self.appointment_repository,
            self.patient_repository,
            self.doctor_repository
        )
        
        # Create sample entities
        self.sample_patient = self._create_sample_patient()
        self.sample_doctor = self._create_sample_doctor()
        self.sample_appointment = self._create_sample_appointment()
    
    def _create_sample_patient(self):
        """Create a sample patient for testing."""
        patient = MagicMock(spec=Patient)
        patient.id = "patient-123"
        return patient
    
    def _create_sample_doctor(self):
        """Create a sample doctor for testing."""
        doctor = MagicMock(spec=Doctor)
        doctor.id = "doctor-123"
        return doctor
    
    def _create_sample_appointment(self):
        """Create a sample appointment for testing."""
        # Create appointment 48 hours in the future
        future_time = datetime.now() + timedelta(hours=48)
        
        appointment = MagicMock(spec=Appointment)
        appointment.id = "appointment-123"
        appointment.patient = self.sample_patient
        appointment.doctor = self.sample_doctor
        appointment.date_time = future_time
        appointment.duration = 30  # 30 minutes
        appointment.status = AppointmentStatus.SCHEDULED
        
        return appointment
    
    def test_create_appointment_success(self):
        """Test creating an appointment successfully."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        self.appointment_repository.find_by_doctor_id.return_value = []
        self.appointment_repository.find_by_patient_id.return_value = []
        
        # Execute
        result = self.appointment_service.create_appointment(self.sample_appointment)
        
        # Verify
        self.patient_repository.find_by_id.assert_called_once_with("patient-123")
        self.doctor_repository.find_by_id.assert_called_once_with("doctor-123")
        self.appointment_repository.find_by_doctor_id.assert_called_once_with("doctor-123")
        self.appointment_repository.find_by_patient_id.assert_called_once_with("patient-123")
        self.appointment_repository.save.assert_called_once_with(self.sample_appointment)
        self.assertEqual(result, self.sample_appointment)
    
    def test_create_appointment_patient_not_found(self):
        """Test creating an appointment with a non-existent patient."""
        # Setup
        self.patient_repository.find_by_id.return_value = None
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(self.sample_appointment)
        
        self.assertIn("Patient", str(context.exception))
        self.assertIn("not found", str(context.exception))
        self.appointment_repository.save.assert_not_called()
    
    def test_create_appointment_doctor_not_found(self):
        """Test creating an appointment with a non-existent doctor."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        self.doctor_repository.find_by_id.return_value = None
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(self.sample_appointment)
        
        self.assertIn("Doctor", str(context.exception))
        self.assertIn("not found", str(context.exception))
        self.appointment_repository.save.assert_not_called()
    
    def test_create_appointment_past_time(self):
        """Test creating an appointment with a past time."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Set appointment time to the past
        past_appointment = MagicMock(spec=Appointment)
        past_appointment.patient = self.sample_patient
        past_appointment.doctor = self.sample_doctor
        past_appointment.date_time = datetime.now() - timedelta(hours=1)
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(past_appointment)
        
        self.assertIn("past", str(context.exception))
        self.appointment_repository.save.assert_not_called()
    
    def test_create_appointment_less_than_24_hours(self):
        """Test creating an appointment less than 24 hours in advance."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Set appointment time to less than 24 hours in the future
        soon_appointment = MagicMock(spec=Appointment)
        soon_appointment.patient = self.sample_patient
        soon_appointment.doctor = self.sample_doctor
        soon_appointment.date_time = datetime.now() + timedelta(hours=12)
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(soon_appointment)
        
        self.assertIn("24 hours", str(context.exception))
        self.appointment_repository.save.assert_not_called()
    
    def test_create_appointment_doctor_already_booked(self):
        """Test creating an appointment when the doctor is already booked."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Create an existing appointment at the same time
        existing_appointment = MagicMock(spec=Appointment)
        existing_appointment.date_time = self.sample_appointment.date_time
        existing_appointment.duration = 30
        existing_appointment.status = AppointmentStatus.SCHEDULED
        
        self.appointment_repository.find_by_doctor_id.return_value = [existing_appointment]
        self.appointment_repository.find_by_patient_id.return_value = []
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(self.sample_appointment)
        
        self.assertIn("already booked", str(context.exception))
        self.appointment_repository.save.assert_not_called()
    
    def test_create_appointment_patient_max_daily_limit(self):
        """Test creating an appointment when the patient has reached the daily limit."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        self.appointment_repository.find_by_doctor_id.return_value = []
        
        # Create three existing appointments on the same day
        appointment_date = self.sample_appointment.date_time.date()
        existing_appointments = []
        
        for i in range(3):
            existing_appointment = MagicMock(spec=Appointment)
            existing_appointment.date_time = datetime.combine(
                appointment_date, 
                datetime.min.time()
            ) + timedelta(hours=i)
            existing_appointment.status = AppointmentStatus.SCHEDULED
            existing_appointments.append(existing_appointment)
        
        self.appointment_repository.find_by_patient_id.return_value = existing_appointments
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(self.sample_appointment)
        
        self.assertIn("3 appointments", str(context.exception))
        self.appointment_repository.save.assert_not_called()
    
    def test_get_appointment(self):
        """Test getting an appointment by ID."""
        # Setup
        self.appointment_repository.find_by_id.return_value = self.sample_appointment
        
        # Execute
        result = self.appointment_service.get_appointment("appointment-123")
        
        # Verify
        self.appointment_repository.find_by_id.assert_called_once_with("appointment-123")
        self.assertEqual(result, self.sample_appointment)
    
    def test_cancel_appointment_success(self):
        """Test cancelling an appointment successfully."""
        # Setup
        self.appointment_repository.find_by_id.return_value = self.sample_appointment
        
        # Execute
        result = self.appointment_service.cancel_appointment("appointment-123")
        
        # Verify
        self.appointment_repository.find_by_id.assert_called_once_with("appointment-123")
        self.assertEqual(result.status, AppointmentStatus.CANCELLED)
        self.appointment_repository.save.assert_called_once()
    
    def test_cancel_appointment_too_late(self):
        """Test cancelling an appointment too close to the scheduled time."""
        # Setup
        soon_appointment = MagicMock(spec=Appointment)
        soon_appointment.date_time = datetime.now() + timedelta(hours=3)
        self.appointment_repository.find_by_id.return_value = soon_appointment
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.appointment_service.cancel_appointment("appointment-123")
        
        self.assertIn("6 hours", str(context.exception))
        self.appointment_repository.save.assert_not_called()

if __name__ == "__main__":
    unittest.main()
