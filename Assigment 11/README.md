# Assignment 11: Implementing a Persistence Repository Layer

This project implements a repository layer to persist domain model objects from Assignment 10. The implementation abstracts storage details behind interfaces, supports CRUD operations, and uses the Factory Pattern to switch between storage implementations.

## Project Structure

- `/repositories`: Contains repository interfaces and implementations
  - `/inmemory`: In-memory implementations using HashMap
  - `/filesystem`: Stub implementation for file system storage
- `/factories`: Contains the repository factory for creating repository instances
- `/src`: Contains the domain model classes from Assignment 10
- `/tests`: Contains unit tests for the repository implementations

## Repository Interface Design

The repository layer uses a generic interface approach to avoid duplication across entity repositories:

```python
class Repository(Generic[T, ID]):
    def save(self, entity: T) -> None: ...
    def find_by_id(self, id: ID) -> Optional[T]: ...
    def find_all(self) -> List[T]: ...
    def delete(self, id: ID) -> None: ...
```

Entity-specific interfaces extend this generic interface to add domain-specific operations:

```python
class PatientRepository(Repository[Patient, str]):
    def find_by_email(self, email: str) -> Optional[Patient]: ...
    def find_by_name(self, name: str) -> List[Patient]: ...
```

**Justification**: Used generics to avoid duplication across entity repositories. This approach allows for type safety and code reuse, while still allowing for entity-specific operations.

## In-Memory Implementation

The in-memory implementation uses a HashMap (dictionary in Python) to store entities:

```python
class BaseInMemoryRepository(Repository[T, ID], Generic[T, ID]):
    def __init__(self):
        self._storage: Dict[ID, T] = {}
    
    def save(self, entity: T) -> None:
        entity_id = self._get_entity_id(entity)
        self._storage[entity_id] = entity
    
    # Other CRUD operations...
```

Entity-specific implementations extend this base class to add domain-specific operations:

```python
class InMemoryPatientRepository(BaseInMemoryRepository[Patient, str], PatientRepository):
    def find_by_email(self, email: str) -> Optional[Patient]:
        for patient in self._storage.values():
            if patient.contact_info.email == email:
                return patient
        return None
    
    # Other domain-specific operations...
```

## Storage-Abstraction Mechanism

This project uses the Factory Pattern to abstract storage details:

```python
class RepositoryFactory:
    _repository_mappings: Dict[Type[R], Dict[StorageType, Type[R]]] = {
        PatientRepository: {
            StorageType.MEMORY: InMemoryPatientRepository,
            # Future implementations...
        },
        # Other repository mappings...
    }
    
    @classmethod
    def get_repository(cls, repository_interface: Type[R], storage_type: StorageType = StorageType.MEMORY, **kwargs) -> R:
        # Implementation...
```

**Justification**: The Factory Pattern was chosen over Dependency Injection (DI) because it provides a centralized way to create repository instances based on the desired storage type. This approach makes it easy to switch between different storage implementations without changing the client code.

## Future-Proofing

The repository layer is designed to be easily extended with new storage backends:

1. **File System Storage**: A stub implementation for storing entities as JSON files is provided in the `/repositories/filesystem` directory.
2. **Database Storage**: The repository factory is designed to support database storage implementations in the future.
3. **External REST APIs**: The repository factory can be extended to support external REST API storage implementations.

To add a new storage backend, you would:

1. Create a new implementation of the repository interfaces
2. Add the implementation to the repository factory mappings
3. Use the factory to create repository instances with the new storage type

## Class Diagram

```
+-------------------+     +------------------------+
| Repository<T, ID> |<|--- | PatientRepository     |
+-------------------+     +------------------------+
         ^                           ^
         |                           |
+------------------------+  +------------------------+
| BaseInMemoryRepository |<-| InMemoryPatientRepo   |
+------------------------+  +------------------------+

+-------------------+     +------------------------+
| Repository<T, ID> |<|--- | DoctorRepository      |
+-------------------+     +------------------------+
         ^                           ^
         |                           |
+------------------------+  +------------------------+
| BaseInMemoryRepository |<-| InMemoryDoctorRepo    |
+------------------------+  +------------------------+

+------------------+
| RepositoryFactory|
+------------------+
| +get_repository()|
+------------------+
```

## Running the Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Future Enhancements

- Implement database storage using SQLAlchemy or another ORM
- Add transaction support for database operations
- Implement caching for frequently accessed entities
- Add pagination support for large result sets
