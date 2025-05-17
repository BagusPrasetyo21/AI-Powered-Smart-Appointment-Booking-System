import json
import os
from datetime import datetime, date
from typing import Optional, List, Dict
from repositories.patient_repository import PatientRepository
from src.patient import Patient
from src.contact_info import ContactInfo

class FileSystemPatientRepository(PatientRepository):
    """
    File system implementation of the PatientRepository interface.
    This is a stub implementation that demonstrates how a file system-based
    repository could be implemented in the future.
    """
    
    def __init__(self, file_path: str):
        """
        Initialize the file system repository.
        
        Args:
            file_path: Path to the JSON file for storing patients
        """
        self._file_path = file_path
        self._ensure_file_exists()
    
    def save(self, entity: Patient) -> None:
        """
        Save a patient to the file system.
        
        Args:
            entity: The patient to save
        """
        patients = self._load_all_as_dict()
        patients[entity.patient_id] = self._serialize_patient(entity)
        self._save_to_file(patients)
    
    def find_by_id(self, id: str) -> Optional[Patient]:
        """
        Find a patient by their ID.
        
        Args:
            id: The ID of the patient to find
            
        Returns:
            The patient if found, None otherwise
        """
        patients = self._load_all_as_dict()
        if id in patients:
            return self._deserialize_patient(patients[id])
        return None
    
    def find_all(self) -> List[Patient]:
        """
        Find all patients.
        
        Returns:
            A list of all patients
        """
        patients = self._load_all_as_dict()
        return [self._deserialize_patient(patient_data) for patient_data in patients.values()]
    
    def delete(self, id: str) -> None:
        """
        Delete a patient by their ID.
        
        Args:
            id: The ID of the patient to delete
        """
        patients = self._load_all_as_dict()
        if id in patients:
            del patients[id]
            self._save_to_file(patients)
    
    def find_by_email(self, email: str) -> Optional[Patient]:
        """
        Find a patient by their email address.
        
        Args:
            email: The email address to search for
            
        Returns:
            The patient if found, None otherwise
        """
        for patient in self.find_all():
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
            patient for patient in self.find_all()
            if name.lower() in patient.name.lower()
        ]
    
    def _ensure_file_exists(self) -> None:
        """Ensure the storage file exists."""
        if not os.path.exists(os.path.dirname(self._file_path)):
            os.makedirs(os.path.dirname(self._file_path))
        
        if not os.path.exists(self._file_path):
            with open(self._file_path, 'w') as f:
                json.dump({}, f)
    
    def _load_all_as_dict(self) -> Dict[str, Dict]:
        """Load all patients from the file as a dictionary."""
        with open(self._file_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    
    def _save_to_file(self, patients: Dict[str, Dict]) -> None:
        """Save patients to the file."""
        with open(self._file_path, 'w') as f:
            json.dump(patients, f, indent=2)
    
    def _serialize_patient(self, patient: Patient) -> Dict:
        """
        Serialize a patient to a dictionary.
        This is a simplified implementation and would need to be expanded
        to handle all patient attributes in a real implementation.
        """
        return {
            'patient_id': patient.patient_id,
            'name': patient.name,
            'date_of_birth': patient.date_of_birth.isoformat() if patient.date_of_birth else None,
            'medical_history_id': patient.medical_history_id,
            'contact_info': {
                'email': patient.email,
                'phone': patient.phone,
                'address': patient.address
            }
            # Additional fields would be added here
        }
    
    def _deserialize_patient(self, data: Dict) -> Patient:
        """
        Deserialize a patient from a dictionary.
        This is a simplified implementation and would need to be expanded
        to handle all patient attributes in a real implementation.
        """
        contact_info = ContactInfo(
            email=data['contact_info']['email'],
            phone=data['contact_info']['phone'],
            address=data['contact_info']['address']
        )
        
        # Parse date of birth if it exists
        dob = None
        if data.get('date_of_birth'):
            dob = datetime.fromisoformat(data['date_of_birth']).date()
        
        patient = Patient(
            patient_id=data['patient_id'],
            name=data['name'],
            date_of_birth=dob,
            medical_history_id=data['medical_history_id'],
            contact_info=contact_info
        )
        
        # Additional fields would be handled here
        
        return patient
