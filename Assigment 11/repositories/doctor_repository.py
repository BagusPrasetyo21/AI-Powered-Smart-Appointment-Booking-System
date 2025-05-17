from typing import Optional, List
from repositories.repository import Repository
from src.doctor import Doctor

class DoctorRepository(Repository[Doctor, str]):
    """
    Repository interface for Doctor entities.
    Extends the generic Repository interface with Doctor-specific operations.
    """
    
    def find_by_specialization(self, specialization: str) -> List[Doctor]:
        """
        Find doctors by their specialization.
        
        Args:
            specialization: The specialization to search for
            
        Returns:
            A list of doctors with the specified specialization
        """
        pass
    
    def find_by_name(self, name: str) -> List[Doctor]:
        """
        Find doctors by their name.
        
        Args:
            name: The name to search for
            
        Returns:
            A list of doctors with matching names
        """
        pass
