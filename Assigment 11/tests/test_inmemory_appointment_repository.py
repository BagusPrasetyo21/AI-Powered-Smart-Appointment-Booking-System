import unittest
from datetime import datetime, timedelta
from src.appointment import Appointment
from src.enums import AppointmentStatus, AppointmentType
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository

class TestInMemoryAppointmentRepository(unittest.TestCase):
    """
    Test case for the InMemoryAppointmentRepository class.
    """
    
    def setUp(self):
        """Set up the test case."""
        self.repository = InMemoryAppointmentRepository()
        
        # Create test appointments
        now = datetime.now()
        
        self.appointment1 = Appointment(
            appointment_id="appointment1",
            patient_id="patient1",
            doctor_id="doctor1",
            date_time=now,
            duration=30,
            appointment_type=AppointmentType.REGULAR,
            status=AppointmentStatus.SCHEDULED,
            notes="Regular checkup"
        )
        
        self.appointment2 = Appointment(
            appointment_id="appointment2",
            patient_id="patient1",
            doctor_id="doctor1",
            date_time=now + timedelta(days=1),
            duration=30,
            appointment_type=AppointmentType.FOLLOW_UP,
            status=AppointmentStatus.SCHEDULED,
            notes="Follow-up"
        )
    
    def test_save_and_find_by_id(self):
        """Test saving an appointment and finding it by ID."""
        # Save an appointment
        self.repository.save(self.appointment1)
        
        # Find the appointment by ID
        found_appointment = self.repository.find_by_id("appointment1")
        
        # Assert that the found appointment is the same as the saved appointment
        self.assertIsNotNone(found_appointment)
        self.assertEqual(found_appointment.appointment_id, self.appointment1.appointment_id)
        self.assertEqual(found_appointment.patient_id, self.appointment1.patient_id)
        self.assertEqual(found_appointment.doctor_id, self.appointment1.doctor_id)
        self.assertEqual(found_appointment.date_time, self.appointment1.date_time)
        self.assertEqual(found_appointment.status, self.appointment1.status)
    
    def test_find_by_id_not_found(self):
        """Test finding an appointment by ID when the appointment does not exist."""
        # Find an appointment that does not exist
        found_appointment = self.repository.find_by_id("nonexistent")
        
        # Assert that the appointment is not found
        self.assertIsNone(found_appointment)
    
    def test_find_all(self):
        """Test finding all appointments."""
        # Save two appointments
        self.repository.save(self.appointment1)
        self.repository.save(self.appointment2)
        
        # Find all appointments
        all_appointments = self.repository.find_all()
        
        # Assert that both appointments are found
        self.assertEqual(len(all_appointments), 2)
        appointment_ids = [a.appointment_id for a in all_appointments]
        self.assertIn(self.appointment1.appointment_id, appointment_ids)
        self.assertIn(self.appointment2.appointment_id, appointment_ids)
    
    def test_delete(self):
        """Test deleting an appointment."""
        # Save an appointment
        self.repository.save(self.appointment1)
        
        # Delete the appointment
        self.repository.delete("appointment1")
        
        # Assert that the appointment is deleted
        self.assertIsNone(self.repository.find_by_id("appointment1"))
    
    def test_find_by_patient_id(self):
        """Test finding appointments by patient ID."""
        # Save two appointments
        self.repository.save(self.appointment1)
        self.repository.save(self.appointment2)
        
        # Find appointments by patient ID
        found_appointments = self.repository.find_by_patient_id("patient1")
        
        # Assert that both appointments are found
        self.assertEqual(len(found_appointments), 2)
        appointment_ids = [a.appointment_id for a in found_appointments]
        self.assertIn(self.appointment1.appointment_id, appointment_ids)
        self.assertIn(self.appointment2.appointment_id, appointment_ids)
    
    def test_find_by_doctor_id(self):
        """Test finding appointments by doctor ID."""
        # Save two appointments
        self.repository.save(self.appointment1)
        self.repository.save(self.appointment2)
        
        # Find appointments by doctor ID
        found_appointments = self.repository.find_by_doctor_id("doctor1")
        
        # Assert that both appointments are found
        self.assertEqual(len(found_appointments), 2)
        appointment_ids = [a.appointment_id for a in found_appointments]
        self.assertIn(self.appointment1.appointment_id, appointment_ids)
        self.assertIn(self.appointment2.appointment_id, appointment_ids)
    
    def test_find_by_date_range(self):
        """Test finding appointments within a date range."""
        # Save two appointments
        self.repository.save(self.appointment1)
        self.repository.save(self.appointment2)
        
        # Find appointments within a date range
        now = datetime.now()
        tomorrow = now + timedelta(days=1)
        found_appointments = self.repository.find_by_date_range(tomorrow, tomorrow + timedelta(days=1))
        
        # Assert that only the second appointment is found
        self.assertEqual(len(found_appointments), 1)
        self.assertEqual(found_appointments[0].appointment_id, self.appointment2.appointment_id)

if __name__ == "__main__":
    unittest.main()
