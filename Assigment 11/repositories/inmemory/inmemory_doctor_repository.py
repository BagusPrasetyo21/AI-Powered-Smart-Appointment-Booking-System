from typing import List
from repositories.inmemory.base_inmemory_repository import BaseInMemoryRepository
from repositories.doctor_repository import DoctorRepository
from src.doctor import Doctor

class InMemoryDoctorRepository(BaseInMemoryRepository[Doctor, str], DoctorRepository):
    """
    In-memory implementation of the DoctorRepository interface.
    """
    
    def _get_entity_id(self, entity: Doctor) -> str:
        """Get the ID of a doctor entity."""
        return entity.doctor_id
    
    def find_by_specialization(self, specialization: str) -> List[Doctor]:
        """
        Find doctors by their specialization.
        
        Args:
            specialization: The specialization to search for
            
        Returns:
            A list of doctors with the specified specialization
        """
        return [
            doctor for doctor in self._storage.values()
            if doctor.specialization == specialization
        ]
    
    def find_by_name(self, name: str) -> List[Doctor]:
        """
        Find doctors by their name.
        
        Args:
            name: The name to search for
            
        Returns:
            A list of doctors with matching names
        """
        return [
            doctor for doctor in self._storage.values()
            if name.lower() in doctor.name.lower()
        ]
