"""
Unit tests for the doctor service.
"""
import unittest
from unittest.mock import Mock, MagicMock
from src.doctor import Doctor
from src.contact_info import ContactInfo
from src.schedule import Schedule
from repositories.doctor_repository import DoctorRepository
from services.doctor_service import DoctorService

class TestDoctorService(unittest.TestCase):
    """
    Test cases for the doctor service.
    """
    
    def setUp(self):
        """Set up test fixtures."""
        self.doctor_repository = Mock(spec=DoctorRepository)
        self.doctor_service = DoctorService(self.doctor_repository)
        
        # Create a sample doctor
        self.sample_doctor = self._create_sample_doctor()
    
    def _create_sample_doctor(self):
        """Create a sample doctor for testing."""
        contact_info = MagicMock(spec=ContactInfo)
        schedule = MagicMock(spec=Schedule)
        
        doctor = MagicMock(spec=Doctor)
        doctor.id = "doctor-123"
        doctor.name = "Dr. Jane Smith"
        doctor.specialization = "Cardiology"
        doctor.contact_info = contact_info
        doctor.schedule = schedule
        
        return doctor
    
    def test_create_doctor_success(self):
        """Test creating a doctor successfully."""
        # Setup
        self.doctor_repository.find_by_id.return_value = None
        
        # Execute
        result = self.doctor_service.create_doctor(self.sample_doctor)
        
        # Verify
        self.doctor_repository.find_by_id.assert_called_once_with("doctor-123")
        self.doctor_repository.save.assert_called_once_with(self.sample_doctor)
        self.assertEqual(result, self.sample_doctor)
    
    def test_create_doctor_duplicate_id(self):
        """Test creating a doctor with a duplicate ID."""
        # Setup
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.doctor_service.create_doctor(self.sample_doctor)
        
        self.assertIn("already exists", str(context.exception))
        self.doctor_repository.save.assert_not_called()
    
    def test_get_doctor(self):
        """Test getting a doctor by ID."""
        # Setup
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Execute
        result = self.doctor_service.get_doctor("doctor-123")
        
        # Verify
        self.doctor_repository.find_by_id.assert_called_once_with("doctor-123")
        self.assertEqual(result, self.sample_doctor)
    
    def test_get_all_doctors(self):
        """Test getting all doctors."""
        # Setup
        doctors = [self.sample_doctor, MagicMock(spec=Doctor)]
        self.doctor_repository.find_all.return_value = doctors
        
        # Execute
        result = self.doctor_service.get_all_doctors()
        
        # Verify
        self.doctor_repository.find_all.assert_called_once()
        self.assertEqual(result, doctors)
    
    def test_update_doctor_success(self):
        """Test updating a doctor successfully."""
        # Setup
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Execute
        result = self.doctor_service.update_doctor(self.sample_doctor)
        
        # Verify
        self.doctor_repository.find_by_id.assert_called_once_with("doctor-123")
        self.doctor_repository.save.assert_called_once_with(self.sample_doctor)
        self.assertEqual(result, self.sample_doctor)
    
    def test_update_doctor_not_found(self):
        """Test updating a non-existent doctor."""
        # Setup
        self.doctor_repository.find_by_id.return_value = None
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.doctor_service.update_doctor(self.sample_doctor)
        
        self.assertIn("not found", str(context.exception))
        self.doctor_repository.save.assert_not_called()
    
    def test_delete_doctor_success(self):
        """Test deleting a doctor successfully."""
        # Setup
        self.doctor_repository.find_by_id.return_value = self.sample_doctor
        
        # Execute
        self.doctor_service.delete_doctor("doctor-123")
        
        # Verify
        self.doctor_repository.find_by_id.assert_called_once_with("doctor-123")
        self.doctor_repository.delete.assert_called_once_with("doctor-123")
    
    def test_delete_doctor_not_found(self):
        """Test deleting a non-existent doctor."""
        # Setup
        self.doctor_repository.find_by_id.return_value = None
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.doctor_service.delete_doctor("doctor-123")
        
        self.assertIn("not found", str(context.exception))
        self.doctor_repository.delete.assert_not_called()
    
    def test_find_doctors_by_specialization(self):
        """Test finding doctors by specialization."""
        # Setup
        doctors = [self.sample_doctor]
        self.doctor_repository.find_by_specialization.return_value = doctors
        
        # Execute
        result = self.doctor_service.find_doctors_by_specialization("Cardiology")
        
        # Verify
        self.doctor_repository.find_by_specialization.assert_called_once_with("Cardiology")
        self.assertEqual(result, doctors)
    
    def test_find_doctors_by_name(self):
        """Test finding doctors by name."""
        # Setup
        doctors = [self.sample_doctor]
        self.doctor_repository.find_by_name.return_value = doctors
        
        # Execute
        result = self.doctor_service.find_doctors_by_name("Smith")
        
        # Verify
        self.doctor_repository.find_by_name.assert_called_once_with("Smith")
        self.assertEqual(result, doctors)

if __name__ == "__main__":
    unittest.main()
