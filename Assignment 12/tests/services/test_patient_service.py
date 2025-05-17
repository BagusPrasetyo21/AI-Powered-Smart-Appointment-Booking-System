"""
Unit tests for the patient service.
"""
import unittest
from unittest.mock import Mock, MagicMock
from src.patient import Patient
from src.contact_info import ContactInfo
from repositories.patient_repository import PatientRepository
from services.patient_service import PatientService

class TestPatientService(unittest.TestCase):
    """
    Test cases for the patient service.
    """
    
    def setUp(self):
        """Set up test fixtures."""
        self.patient_repository = Mock(spec=PatientRepository)
        self.patient_service = PatientService(self.patient_repository)
        
        # Create a sample patient
        self.sample_patient = self._create_sample_patient()
    
    def _create_sample_patient(self):
        """Create a sample patient for testing."""
        contact_info = MagicMock(spec=ContactInfo)
        contact_info.email = "john.doe@example.com"
        
        patient = MagicMock(spec=Patient)
        patient.id = "patient-123"
        patient.name = "John Doe"
        patient.contact_info = contact_info
        
        return patient
    
    def test_create_patient_success(self):
        """Test creating a patient successfully."""
        # Setup
        self.patient_repository.find_by_email.return_value = None
        
        # Execute
        result = self.patient_service.create_patient(self.sample_patient)
        
        # Verify
        self.patient_repository.find_by_email.assert_called_once_with("john.doe@example.com")
        self.patient_repository.save.assert_called_once_with(self.sample_patient)
        self.assertEqual(result, self.sample_patient)
    
    def test_create_patient_duplicate_email(self):
        """Test creating a patient with a duplicate email."""
        # Setup
        self.patient_repository.find_by_email.return_value = self.sample_patient
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.patient_service.create_patient(self.sample_patient)
        
        self.assertIn("already exists", str(context.exception))
        self.patient_repository.save.assert_not_called()
    
    def test_get_patient(self):
        """Test getting a patient by ID."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        
        # Execute
        result = self.patient_service.get_patient("patient-123")
        
        # Verify
        self.patient_repository.find_by_id.assert_called_once_with("patient-123")
        self.assertEqual(result, self.sample_patient)
    
    def test_get_all_patients(self):
        """Test getting all patients."""
        # Setup
        patients = [self.sample_patient, MagicMock(spec=Patient)]
        self.patient_repository.find_all.return_value = patients
        
        # Execute
        result = self.patient_service.get_all_patients()
        
        # Verify
        self.patient_repository.find_all.assert_called_once()
        self.assertEqual(result, patients)
    
    def test_update_patient_success(self):
        """Test updating a patient successfully."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        
        # Execute
        result = self.patient_service.update_patient(self.sample_patient)
        
        # Verify
        self.patient_repository.find_by_id.assert_called_once_with("patient-123")
        self.patient_repository.save.assert_called_once_with(self.sample_patient)
        self.assertEqual(result, self.sample_patient)
    
    def test_update_patient_not_found(self):
        """Test updating a non-existent patient."""
        # Setup
        self.patient_repository.find_by_id.return_value = None
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.patient_service.update_patient(self.sample_patient)
        
        self.assertIn("not found", str(context.exception))
        self.patient_repository.save.assert_not_called()
    
    def test_delete_patient_success(self):
        """Test deleting a patient successfully."""
        # Setup
        self.patient_repository.find_by_id.return_value = self.sample_patient
        
        # Execute
        self.patient_service.delete_patient("patient-123")
        
        # Verify
        self.patient_repository.find_by_id.assert_called_once_with("patient-123")
        self.patient_repository.delete.assert_called_once_with("patient-123")
    
    def test_delete_patient_not_found(self):
        """Test deleting a non-existent patient."""
        # Setup
        self.patient_repository.find_by_id.return_value = None
        
        # Execute and verify
        with self.assertRaises(ValueError) as context:
            self.patient_service.delete_patient("patient-123")
        
        self.assertIn("not found", str(context.exception))
        self.patient_repository.delete.assert_not_called()
    
    def test_find_patients_by_name(self):
        """Test finding patients by name."""
        # Setup
        patients = [self.sample_patient]
        self.patient_repository.find_by_name.return_value = patients
        
        # Execute
        result = self.patient_service.find_patients_by_name("John")
        
        # Verify
        self.patient_repository.find_by_name.assert_called_once_with("John")
        self.assertEqual(result, patients)

if __name__ == "__main__":
    unittest.main()
