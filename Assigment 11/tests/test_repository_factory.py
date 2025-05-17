import unittest
from factories.repository_factory import RepositoryFactory, StorageType
from repositories.patient_repository import PatientRepository
from repositories.doctor_repository import DoctorRepository
from repositories.appointment_repository import AppointmentRepository
from repositories.inmemory.inmemory_patient_repository import InMemoryPatientRepository
from repositories.inmemory.inmemory_doctor_repository import InMemoryDoctorRepository
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository

class TestRepositoryFactory(unittest.TestCase):
    """
    Test case for the RepositoryFactory class.
    """
    
    def test_get_patient_repository(self):
        """Test getting a patient repository."""
        # Get a patient repository with memory storage
        repository = RepositoryFactory.get_repository(PatientRepository, StorageType.MEMORY)
        
        # Assert that the repository is an instance of InMemoryPatientRepository
        self.assertIsInstance(repository, InMemoryPatientRepository)
    
    def test_get_doctor_repository(self):
        """Test getting a doctor repository."""
        # Get a doctor repository with memory storage
        repository = RepositoryFactory.get_repository(DoctorRepository, StorageType.MEMORY)
        
        # Assert that the repository is an instance of InMemoryDoctorRepository
        self.assertIsInstance(repository, InMemoryDoctorRepository)
    
    def test_get_appointment_repository(self):
        """Test getting an appointment repository."""
        # Get an appointment repository with memory storage
        repository = RepositoryFactory.get_repository(AppointmentRepository, StorageType.MEMORY)
        
        # Assert that the repository is an instance of InMemoryAppointmentRepository
        self.assertIsInstance(repository, InMemoryAppointmentRepository)
    
    def test_get_repository_with_unsupported_interface(self):
        """Test getting a repository with an unsupported interface."""
        # Define a dummy class that doesn't extend Repository
        class DummyClass:
            pass
        
        # Assert that getting a repository with an unsupported interface raises a ValueError
        with self.assertRaises(ValueError):
            RepositoryFactory.get_repository(DummyClass, StorageType.MEMORY)
    
    def test_get_repository_with_unsupported_storage_type(self):
        """Test getting a repository with an unsupported storage type."""
        # Assert that getting a repository with an unsupported storage type raises a ValueError
        with self.assertRaises(ValueError):
            RepositoryFactory.get_repository(PatientRepository, StorageType.DATABASE)

if __name__ == "__main__":
    unittest.main()
