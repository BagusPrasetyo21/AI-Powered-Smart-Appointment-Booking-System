from enum import Enum
from typing import Dict, Type, TypeVar, Generic

from repositories.repository import Repository
from repositories.patient_repository import PatientRepository
from repositories.doctor_repository import DoctorRepository
from repositories.appointment_repository import AppointmentRepository

from repositories.inmemory.inmemory_patient_repository import InMemoryPatientRepository
from repositories.inmemory.inmemory_doctor_repository import InMemoryDoctorRepository
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository

# Define storage types
class StorageType(Enum):
    MEMORY = "MEMORY"
    DATABASE = "DATABASE"
    FILE_SYSTEM = "FILE_SYSTEM"

# Type variable for repository interfaces
R = TypeVar('R', bound=Repository)

class RepositoryFactory:
    """
    Factory class for creating repository instances.
    This allows for easy switching between different storage implementations.
    """
    
    # Dictionary to store repository mappings
    _repository_mappings: Dict[Type[R], Dict[StorageType, Type[R]]] = {
        PatientRepository: {
            StorageType.MEMORY: InMemoryPatientRepository,
            # Future implementations will be added here
            # StorageType.DATABASE: DatabasePatientRepository,
            # StorageType.FILE_SYSTEM: FileSystemPatientRepository,
        },
        DoctorRepository: {
            StorageType.MEMORY: InMemoryDoctorRepository,
            # Future implementations will be added here
            # StorageType.DATABASE: DatabaseDoctorRepository,
            # StorageType.FILE_SYSTEM: FileSystemDoctorRepository,
        },
        AppointmentRepository: {
            StorageType.MEMORY: InMemoryAppointmentRepository,
            # Future implementations will be added here
            # StorageType.DATABASE: DatabaseAppointmentRepository,
            # StorageType.FILE_SYSTEM: FileSystemAppointmentRepository,
        },
    }
    
    @classmethod
    def get_repository(cls, repository_interface: Type[R], storage_type: StorageType = StorageType.MEMORY, **kwargs) -> R:
        """
        Get a repository instance for the specified interface and storage type.
        
        Args:
            repository_interface: The repository interface class
            storage_type: The storage type to use (default: MEMORY)
            **kwargs: Additional arguments to pass to the repository constructor
            
        Returns:
            A repository instance
            
        Raises:
            ValueError: If the repository interface or storage type is not supported
        """
        if repository_interface not in cls._repository_mappings:
            raise ValueError(f"Unsupported repository interface: {repository_interface.__name__}")
        
        storage_mappings = cls._repository_mappings[repository_interface]
        if storage_type not in storage_mappings:
            raise ValueError(f"Unsupported storage type {storage_type} for {repository_interface.__name__}")
        
        repository_class = storage_mappings[storage_type]
        return repository_class(**kwargs)
