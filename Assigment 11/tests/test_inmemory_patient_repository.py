import unittest
from datetime import datetime
from src.patient import Patient
from src.contact_info import ContactInfo
from repositories.inmemory.inmemory_patient_repository import InMemoryPatientRepository

class TestInMemoryPatientRepository(unittest.TestCase):
    """
    Test case for the InMemoryPatientRepository class.
    """
    
    def setUp(self):
        """Set up the test case."""
        self.repository = InMemoryPatientRepository()
        
        # Create test patients
        contact_info1 = ContactInfo(
            email="john.doe@example.com",
            phone="123-456-7890",
            address="123 Main St, Anytown, USA"
        )
        self.patient1 = Patient(
            patient_id="patient1",
            name="John Doe",
            date_of_birth=datetime(1980, 1, 1).date(),
            medical_history_id="mh1",
            contact_info=contact_info1
        )
        
        contact_info2 = ContactInfo(
            email="jane.smith@example.com",
            phone="987-654-3210",
            address="456 Oak St, Anytown, USA"
        )
        self.patient2 = Patient(
            patient_id="patient2",
            name="Jane Smith",
            date_of_birth=datetime(1985, 5, 15).date(),
            medical_history_id="mh2",
            contact_info=contact_info2
        )
    
    def test_save_and_find_by_id(self):
        """Test saving a patient and finding it by ID."""
        # Save a patient
        self.repository.save(self.patient1)
        
        # Find the patient by ID
        found_patient = self.repository.find_by_id("patient1")
        
        # Assert that the found patient is the same as the saved patient
        self.assertIsNotNone(found_patient)
        self.assertEqual(found_patient.patient_id, self.patient1.patient_id)
        self.assertEqual(found_patient.name, self.patient1.name)
        self.assertEqual(found_patient.date_of_birth, self.patient1.date_of_birth)
        self.assertEqual(found_patient.email, self.patient1.email)
    
    def test_find_by_id_not_found(self):
        """Test finding a patient by ID when the patient does not exist."""
        # Find a patient that does not exist
        found_patient = self.repository.find_by_id("nonexistent")
        
        # Assert that the patient is not found
        self.assertIsNone(found_patient)
    
    def test_find_all(self):
        """Test finding all patients."""
        # Save two patients
        self.repository.save(self.patient1)
        self.repository.save(self.patient2)
        
        # Find all patients
        all_patients = self.repository.find_all()
        
        # Assert that both patients are found
        self.assertEqual(len(all_patients), 2)
        patient_ids = [p.patient_id for p in all_patients]
        self.assertIn(self.patient1.patient_id, patient_ids)
        self.assertIn(self.patient2.patient_id, patient_ids)
    
    def test_delete(self):
        """Test deleting a patient."""
        # Save a patient
        self.repository.save(self.patient1)
        
        # Delete the patient
        self.repository.delete("patient1")
        
        # Assert that the patient is deleted
        self.assertIsNone(self.repository.find_by_id("patient1"))
    
    def test_find_by_email(self):
        """Test finding a patient by email."""
        # Save two patients
        self.repository.save(self.patient1)
        self.repository.save(self.patient2)
        
        # Find a patient by email
        found_patient = self.repository.find_by_email("john.doe@example.com")
        
        # Assert that the correct patient is found
        self.assertIsNotNone(found_patient)
        self.assertEqual(found_patient.patient_id, self.patient1.patient_id)
    
    def test_find_by_name(self):
        """Test finding patients by name."""
        # Save two patients
        self.repository.save(self.patient1)
        self.repository.save(self.patient2)
        
        # Find patients by name
        found_patients = self.repository.find_by_name("John")
        
        # Assert that the correct patient is found
        self.assertEqual(len(found_patients), 1)
        self.assertEqual(found_patients[0].patient_id, self.patient1.patient_id)

if __name__ == "__main__":
    unittest.main()
