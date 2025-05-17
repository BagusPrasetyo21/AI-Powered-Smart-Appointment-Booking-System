from typing import Generic, TypeVar, Dict, List, Optional
from repositories.repository import Repository

T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type

class BaseInMemoryRepository(Repository[T, ID], Generic[T, ID]):
    """
    Base in-memory implementation of the Repository interface.
    Uses a HashMap (dictionary) for storage.
    """
    
    def __init__(self):
        """Initialize the in-memory storage."""
        self._storage: Dict[ID, T] = {}
    
    def save(self, entity: T) -> None:
        """
        Save an entity to the in-memory storage.
        
        Args:
            entity: The entity to save
        """
        # We assume entity has an id attribute or property
        entity_id = self._get_entity_id(entity)
        self._storage[entity_id] = entity
    
    def find_by_id(self, id: ID) -> Optional[T]:
        """
        Find an entity by its ID.
        
        Args:
            id: The ID of the entity to find
            
        Returns:
            The entity if found, None otherwise
        """
        return self._storage.get(id)
    
    def find_all(self) -> List[T]:
        """
        Find all entities in the repository.
        
        Returns:
            A list of all entities
        """
        return list(self._storage.values())
    
    def delete(self, id: ID) -> None:
        """
        Delete an entity by its ID.
        
        Args:
            id: The ID of the entity to delete
        """
        if id in self._storage:
            del self._storage[id]
    
    def _get_entity_id(self, entity: T) -> ID:
        """
        Get the ID of an entity.
        This method should be overridden by subclasses if the entity's ID
        is not accessible via the 'id' attribute.
        
        Args:
            entity: The entity to get the ID from
            
        Returns:
            The ID of the entity
        """
        return getattr(entity, 'id')
