"""
Doctor service implementation for handling business logic related to doctors.
"""
from typing import List, Optional
from src.doctor import Doctor
from repositories.doctor_repository import DoctorRepository

class DoctorService:
    """
    Service class for handling business logic related to doctors.
    """
    
    def __init__(self, doctor_repository: DoctorRepository):
        """
        Initialize the doctor service with a repository.
        
        Args:
            doctor_repository: Repository for doctor data access
        """
        self.doctor_repository = doctor_repository
    
    def create_doctor(self, doctor: Doctor) -> Doctor:
        """
        Create a new doctor.
        
        Args:
            doctor: The doctor to create
            
        Returns:
            The created doctor
        
        Raises:
            ValueError: If a doctor with the same ID already exists
        """
        existing_doctor = self.doctor_repository.find_by_id(doctor.id)
        if existing_doctor:
            raise ValueError(f"Doctor with ID {doctor.id} already exists")
        
        # Save the doctor
        self.doctor_repository.save(doctor)
        return doctor
    
    def get_doctor(self, doctor_id: str) -> Optional[Doctor]:
        """
        Get a doctor by ID.
        
        Args:
            doctor_id: The ID of the doctor to get
            
        Returns:
            The doctor if found, None otherwise
        """
        return self.doctor_repository.find_by_id(doctor_id)
    
    def get_all_doctors(self) -> List[Doctor]:
        """
        Get all doctors.
        
        Returns:
            A list of all doctors
        """
        return self.doctor_repository.find_all()
    
    def update_doctor(self, doctor: Doctor) -> Doctor:
        """
        Update an existing doctor.
        
        Args:
            doctor: The doctor to update
            
        Returns:
            The updated doctor
            
        Raises:
            ValueError: If the doctor does not exist
        """
        existing_doctor = self.doctor_repository.find_by_id(doctor.id)
        if not existing_doctor:
            raise ValueError(f"Doctor with ID {doctor.id} not found")
        
        # Save the updated doctor
        self.doctor_repository.save(doctor)
        return doctor
    
    def delete_doctor(self, doctor_id: str) -> None:
        """
        Delete a doctor.
        
        Args:
            doctor_id: The ID of the doctor to delete
            
        Raises:
            ValueError: If the doctor does not exist
        """
        existing_doctor = self.doctor_repository.find_by_id(doctor_id)
        if not existing_doctor:
            raise ValueError(f"Doctor with ID {doctor_id} not found")
        
        self.doctor_repository.delete(doctor_id)
    
    def find_doctors_by_specialization(self, specialization: str) -> List[Doctor]:
        """
        Find doctors by specialization.
        
        Args:
            specialization: The specialization to search for
            
        Returns:
            A list of doctors with the specified specialization
        """
        return self.doctor_repository.find_by_specialization(specialization)
    
    def find_doctors_by_name(self, name: str) -> List[Doctor]:
        """
        Find doctors by name.
        
        Args:
            name: The name to search for
            
        Returns:
            A list of doctors with matching names
        """
        return self.doctor_repository.find_by_name(name)
