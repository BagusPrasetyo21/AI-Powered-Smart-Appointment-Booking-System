from typing import Optional, List
from repositories.repository import Repository
from src.patient import Patient

class PatientRepository(Repository[Patient, str]):
    """
    Repository interface for Patient entities.
    Extends the generic Repository interface with Patient-specific operations.
    """
    
    def find_by_email(self, email: str) -> Optional[Patient]:
        """
        Find a patient by their email address.
        
        Args:
            email: The email address to search for
            
        Returns:
            The patient if found, None otherwise
        """
        pass
    
    def find_by_name(self, name: str) -> List[Patient]:
        """
        Find patients by their name.
        
        Args:
            name: The name to search for
            
        Returns:
            A list of patients with matching names
        """
        pass
