from typing import Generic, TypeVar, List, Optional

# Type variables for generic repository
T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type

class Repository(Generic[T, ID]):
    """
    Generic repository interface with standard CRUD operations.
    This interface defines the contract for all repository implementations.
    """
    
    def save(self, entity: T) -> None:
        """
        Create or update an entity in the repository.
        
        Args:
            entity: The entity to save
        """
        pass
    
    def find_by_id(self, id: ID) -> Optional[T]:
        """
        Find an entity by its ID.
        
        Args:
            id: The ID of the entity to find
            
        Returns:
            The entity if found, None otherwise
        """
        pass
    
    def find_all(self) -> List[T]:
        """
        Find all entities in the repository.
        
        Returns:
            A list of all entities
        """
        pass
    
    def delete(self, id: ID) -> None:
        """
        Delete an entity by its ID.
        
        Args:
            id: The ID of the entity to delete
        """
        pass
