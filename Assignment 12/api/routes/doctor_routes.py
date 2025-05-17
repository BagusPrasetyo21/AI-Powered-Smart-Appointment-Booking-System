"""
API routes for doctor management.
"""
from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from api.models import DoctorCreate, DoctorResponse, DoctorUpdate
from services.doctor_service import DoctorService
from api.main import get_doctor_service

# Create factories for domain objects
from src.contact_info import ContactInfo
from src.doctor import Doctor
from src.schedule import Schedule
from creational_patterns.simple_factory import ContactInfoFactory, DoctorFactory

router = APIRouter()

@router.post("/doctors", response_model=DoctorResponse, status_code=status.HTTP_201_CREATED)
async def create_doctor(
    doctor_data: DoctorCreate,
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Create a new doctor.
    """
    try:
        # Create domain objects using factories
        contact_info = ContactInfoFactory.create_contact_info(
            email=doctor_data.contact_info.email,
            phone=doctor_data.contact_info.phone,
            address=doctor_data.contact_info.address
        )
        
        # Create a default schedule
        schedule = Schedule()
        
        doctor = DoctorFactory.create_doctor(
            name=doctor_data.name,
            specialization=doctor_data.specialization,
            contact_info=contact_info,
            schedule=schedule
        )
        
        # Create the doctor using the service
        created_doctor = doctor_service.create_doctor(doctor)
        
        # Convert to response model
        return {
            "id": created_doctor.id,
            "name": created_doctor.name,
            "specialization": created_doctor.specialization,
            "contact_info": {
                "email": created_doctor.contact_info.email,
                "phone": created_doctor.contact_info.phone,
                "address": created_doctor.contact_info.address
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/doctors", response_model=List[DoctorResponse])
async def get_all_doctors(
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Get all doctors.
    """
    doctors = doctor_service.get_all_doctors()
    
    # Convert to response models
    return [
        {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "contact_info": {
                "email": doctor.contact_info.email,
                "phone": doctor.contact_info.phone,
                "address": doctor.contact_info.address
            }
        }
        for doctor in doctors
    ]

@router.get("/doctors/{doctor_id}", response_model=DoctorResponse)
async def get_doctor(
    doctor_id: str,
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Get a doctor by ID.
    """
    doctor = doctor_service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Doctor with ID {doctor_id} not found"
        )
    
    # Convert to response model
    return {
        "id": doctor.id,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "contact_info": {
            "email": doctor.contact_info.email,
            "phone": doctor.contact_info.phone,
            "address": doctor.contact_info.address
        }
    }

@router.put("/doctors/{doctor_id}", response_model=DoctorResponse)
async def update_doctor(
    doctor_id: str,
    doctor_data: DoctorUpdate,
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Update a doctor.
    """
    try:
        # Get the existing doctor
        existing_doctor = doctor_service.get_doctor(doctor_id)
        if not existing_doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Doctor with ID {doctor_id} not found"
            )
        
        # Update the doctor properties
        if doctor_data.name:
            existing_doctor.name = doctor_data.name
        
        if doctor_data.specialization:
            existing_doctor.specialization = doctor_data.specialization
        
        if doctor_data.contact_info:
            existing_doctor.contact_info.email = doctor_data.contact_info.email
            existing_doctor.contact_info.phone = doctor_data.contact_info.phone
            existing_doctor.contact_info.address = doctor_data.contact_info.address
        
        # Update the doctor using the service
        updated_doctor = doctor_service.update_doctor(existing_doctor)
        
        # Convert to response model
        return {
            "id": updated_doctor.id,
            "name": updated_doctor.name,
            "specialization": updated_doctor.specialization,
            "contact_info": {
                "email": updated_doctor.contact_info.email,
                "phone": updated_doctor.contact_info.phone,
                "address": updated_doctor.contact_info.address
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/doctors/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(
    doctor_id: str,
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Delete a doctor.
    """
    try:
        doctor_service.delete_doctor(doctor_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
    return None

@router.get("/doctors/specialization/{specialization}", response_model=List[DoctorResponse])
async def search_doctors_by_specialization(
    specialization: str,
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Search for doctors by specialization.
    """
    doctors = doctor_service.find_doctors_by_specialization(specialization)
    
    # Convert to response models
    return [
        {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "contact_info": {
                "email": doctor.contact_info.email,
                "phone": doctor.contact_info.phone,
                "address": doctor.contact_info.address
            }
        }
        for doctor in doctors
    ]

@router.get("/doctors/search/{name}", response_model=List[DoctorResponse])
async def search_doctors_by_name(
    name: str,
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Search for doctors by name.
    """
    doctors = doctor_service.find_doctors_by_name(name)
    
    # Convert to response models
    return [
        {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "contact_info": {
                "email": doctor.contact_info.email,
                "phone": doctor.contact_info.phone,
                "address": doctor.contact_info.address
            }
        }
        for doctor in doctors
    ]
