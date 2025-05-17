import unittest
from src.doctor import Doctor
from src.contact_info import ContactInfo
from repositories.inmemory.inmemory_doctor_repository import InMemoryDoctorRepository

class TestInMemoryDoctorRepository(unittest.TestCase):
    """
    Test case for the InMemoryDoctorRepository class.
    """
    
    def setUp(self):
        """Set up the test case."""
        self.repository = InMemoryDoctorRepository()
        
        # Create test doctors
        contact_info1 = ContactInfo(
            email="dr.smith@example.com",
            phone="123-456-7890",
            address="123 Medical Center, Anytown, USA"
        )
        self.doctor1 = Doctor(
            doctor_id="doctor1",
            name="Dr. Smith",
            specialization="Cardiology",
            department="Cardiology",
            license_number="LIC123",
            contact_info=contact_info1
        )
        
        contact_info2 = ContactInfo(
            email="dr.jones@example.com",
            phone="987-654-3210",
            address="456 Hospital St, Anytown, USA"
        )
        self.doctor2 = Doctor(
            doctor_id="doctor2",
            name="Dr. Jones",
            specialization="Neurology",
            department="Neurology",
            license_number="LIC456",
            contact_info=contact_info2
        )
    
    def test_save_and_find_by_id(self):
        """Test saving a doctor and finding it by ID."""
        # Save a doctor
        self.repository.save(self.doctor1)
        
        # Find the doctor by ID
        found_doctor = self.repository.find_by_id("doctor1")
        
        # Assert that the found doctor is the same as the saved doctor
        self.assertIsNotNone(found_doctor)
        self.assertEqual(found_doctor.doctor_id, self.doctor1.doctor_id)
        self.assertEqual(found_doctor.name, self.doctor1.name)
        self.assertEqual(found_doctor.specialization, self.doctor1.specialization)
        self.assertEqual(found_doctor.email, self.doctor1.email)
    
    def test_find_by_id_not_found(self):
        """Test finding a doctor by ID when the doctor does not exist."""
        # Find a doctor that does not exist
        found_doctor = self.repository.find_by_id("nonexistent")
        
        # Assert that the doctor is not found
        self.assertIsNone(found_doctor)
    
    def test_find_all(self):
        """Test finding all doctors."""
        # Save two doctors
        self.repository.save(self.doctor1)
        self.repository.save(self.doctor2)
        
        # Find all doctors
        all_doctors = self.repository.find_all()
        
        # Assert that both doctors are found
        self.assertEqual(len(all_doctors), 2)
        doctor_ids = [d.doctor_id for d in all_doctors]
        self.assertIn(self.doctor1.doctor_id, doctor_ids)
        self.assertIn(self.doctor2.doctor_id, doctor_ids)
    
    def test_delete(self):
        """Test deleting a doctor."""
        # Save a doctor
        self.repository.save(self.doctor1)
        
        # Delete the doctor
        self.repository.delete("doctor1")
        
        # Assert that the doctor is deleted
        self.assertIsNone(self.repository.find_by_id("doctor1"))
    
    def test_find_by_specialization(self):
        """Test finding doctors by specialization."""
        # Save two doctors
        self.repository.save(self.doctor1)
        self.repository.save(self.doctor2)
        
        # Find doctors by specialization
        found_doctors = self.repository.find_by_specialization("Cardiology")
        
        # Assert that the correct doctor is found
        self.assertEqual(len(found_doctors), 1)
        self.assertEqual(found_doctors[0].doctor_id, self.doctor1.doctor_id)
    
    def test_find_by_name(self):
        """Test finding doctors by name."""
        # Save two doctors
        self.repository.save(self.doctor1)
        self.repository.save(self.doctor2)
        
        # Find doctors by name
        found_doctors = self.repository.find_by_name("Smith")
        
        # Assert that the correct doctor is found
        self.assertEqual(len(found_doctors), 1)
        self.assertEqual(found_doctors[0].doctor_id, self.doctor1.doctor_id)

if __name__ == "__main__":
    unittest.main()
