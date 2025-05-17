"""
API routes for patient management.
"""
from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from api.models import PatientCreate, PatientResponse, PatientUpdate
from services.patient_service import PatientService
from api.main import get_patient_service

# Create factories for domain objects
from src.contact_info import ContactInfo
from src.patient import Patient
from creational_patterns.simple_factory import ContactInfoFactory, PatientFactory

router = APIRouter()

@router.post("/patients", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
async def create_patient(
    patient_data: PatientCreate,
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Create a new patient.
    """
    try:
        # Create domain objects using factories
        contact_info = ContactInfoFactory.create_contact_info(
            email=patient_data.contact_info.email,
            phone=patient_data.contact_info.phone,
            address=patient_data.contact_info.address
        )
        
        patient = PatientFactory.create_patient(
            name=patient_data.name,
            contact_info=contact_info
        )
        
        # Create the patient using the service
        created_patient = patient_service.create_patient(patient)
        
        # Convert to response model
        return {
            "id": created_patient.id,
            "name": created_patient.name,
            "contact_info": {
                "email": created_patient.contact_info.email,
                "phone": created_patient.contact_info.phone,
                "address": created_patient.contact_info.address
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/patients", response_model=List[PatientResponse])
async def get_all_patients(
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Get all patients.
    """
    patients = patient_service.get_all_patients()
    
    # Convert to response models
    return [
        {
            "id": patient.id,
            "name": patient.name,
            "contact_info": {
                "email": patient.contact_info.email,
                "phone": patient.contact_info.phone,
                "address": patient.contact_info.address
            }
        }
        for patient in patients
    ]

@router.get("/patients/{patient_id}", response_model=PatientResponse)
async def get_patient(
    patient_id: str,
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Get a patient by ID.
    """
    patient = patient_service.get_patient(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    # Convert to response model
    return {
        "id": patient.id,
        "name": patient.name,
        "contact_info": {
            "email": patient.contact_info.email,
            "phone": patient.contact_info.phone,
            "address": patient.contact_info.address
        }
    }

@router.put("/patients/{patient_id}", response_model=PatientResponse)
async def update_patient(
    patient_id: str,
    patient_data: PatientUpdate,
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Update a patient.
    """
    try:
        # Get the existing patient
        existing_patient = patient_service.get_patient(patient_id)
        if not existing_patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Patient with ID {patient_id} not found"
            )
        
        # Update the patient properties
        if patient_data.name:
            existing_patient.name = patient_data.name
        
        if patient_data.contact_info:
            existing_patient.contact_info.email = patient_data.contact_info.email
            existing_patient.contact_info.phone = patient_data.contact_info.phone
            existing_patient.contact_info.address = patient_data.contact_info.address
        
        # Update the patient using the service
        updated_patient = patient_service.update_patient(existing_patient)
        
        # Convert to response model
        return {
            "id": updated_patient.id,
            "name": updated_patient.name,
            "contact_info": {
                "email": updated_patient.contact_info.email,
                "phone": updated_patient.contact_info.phone,
                "address": updated_patient.contact_info.address
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(
    patient_id: str,
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Delete a patient.
    """
    try:
        patient_service.delete_patient(patient_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
    return None

@router.get("/patients/search/{name}", response_model=List[PatientResponse])
async def search_patients_by_name(
    name: str,
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Search for patients by name.
    """
    patients = patient_service.find_patients_by_name(name)
    
    # Convert to response models
    return [
        {
            "id": patient.id,
            "name": patient.name,
            "contact_info": {
                "email": patient.contact_info.email,
                "phone": patient.contact_info.phone,
                "address": patient.contact_info.address
            }
        }
        for patient in patients
    ]
