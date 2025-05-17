"""
Patient service implementation for handling business logic related to patients.
"""
from typing import List, Optional
from src.patient import Patient
from repositories.patient_repository import PatientRepository

class PatientService:
    """
    Service class for handling business logic related to patients.
    """
    
    def __init__(self, patient_repository: PatientRepository):
        """
        Initialize the patient service with a repository.
        
        Args:
            patient_repository: Repository for patient data access
        """
        self.patient_repository = patient_repository
    
    def create_patient(self, patient: Patient) -> Patient:
        """
        Create a new patient.
        
        Args:
            patient: The patient to create
            
        Returns:
            The created patient
        
        Raises:
            ValueError: If a patient with the same email already exists
        """
        # Check if patient with the same email already exists
        existing_patient = self.patient_repository.find_by_email(patient.contact_info.email)
        if existing_patient:
            raise ValueError(f"Patient with email {patient.contact_info.email} already exists")
        
        # Save the patient
        self.patient_repository.save(patient)
        return patient
    
    def get_patient(self, patient_id: str) -> Optional[Patient]:
        """
        Get a patient by ID.
        
        Args:
            patient_id: The ID of the patient to get
            
        Returns:
            The patient if found, None otherwise
        """
        return self.patient_repository.find_by_id(patient_id)
    
    def get_all_patients(self) -> List[Patient]:
        """
        Get all patients.
        
        Returns:
            A list of all patients
        """
        return self.patient_repository.find_all()
    
    def update_patient(self, patient: Patient) -> Patient:
        """
        Update an existing patient.
        
        Args:
            patient: The patient to update
            
        Returns:
            The updated patient
            
        Raises:
            ValueError: If the patient does not exist
        """
        existing_patient = self.patient_repository.find_by_id(patient.id)
        if not existing_patient:
            raise ValueError(f"Patient with ID {patient.id} not found")
        
        # Save the updated patient
        self.patient_repository.save(patient)
        return patient
    
    def delete_patient(self, patient_id: str) -> None:
        """
        Delete a patient.
        
        Args:
            patient_id: The ID of the patient to delete
            
        Raises:
            ValueError: If the patient does not exist
        """
        existing_patient = self.patient_repository.find_by_id(patient_id)
        if not existing_patient:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        self.patient_repository.delete(patient_id)
    
    def find_patients_by_name(self, name: str) -> List[Patient]:
        """
        Find patients by name.
        
        Args:
            name: The name to search for
            
        Returns:
            A list of patients with matching names
        """
        return self.patient_repository.find_by_name(name)
