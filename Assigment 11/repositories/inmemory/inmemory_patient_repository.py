from typing import Optional, List
from repositories.inmemory.base_inmemory_repository import BaseInMemoryRepository
from repositories.patient_repository import PatientRepository
from src.patient import Patient

class InMemoryPatientRepository(BaseInMemoryRepository[Patient, str], PatientRepository):
    """
    In-memory implementation of the PatientRepository interface.
    """
    
    def _get_entity_id(self, entity: Patient) -> str:
        """Get the ID of a patient entity."""
        return entity.patient_id
    
    def find_by_email(self, email: str) -> Optional[Patient]:
        """
        Find a patient by their email address.
        
        Args:
            email: The email address to search for
            
        Returns:
            The patient if found, None otherwise
        """
        for patient in self._storage.values():
            if patient.email == email:
                return patient
        return None
    
    def find_by_name(self, name: str) -> List[Patient]:
        """
        Find patients by their name.
        
        Args:
            name: The name to search for
            
        Returns:
            A list of patients with matching names
        """
        return [
            patient for patient in self._storage.values()
            if name.lower() in patient.name.lower()
        ]
