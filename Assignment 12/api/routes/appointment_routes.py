"""
API routes for appointment management.
"""
from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from datetime import datetime

from api.models import AppointmentCreate, AppointmentResponse, AppointmentUpdate, AppointmentStatusEnum, AppointmentTypeEnum
from services.appointment_service import AppointmentService
from services.patient_service import PatientService
from services.doctor_service import DoctorService
from api.main import get_appointment_service, get_patient_service, get_doctor_service

# Create factories for domain objects
from src.appointment import Appointment
from src.enums import AppointmentStatus, AppointmentType
from creational_patterns.simple_factory import AppointmentFactory

router = APIRouter()

@router.post("/appointments", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def create_appointment(
    appointment_data: AppointmentCreate,
    appointment_service: AppointmentService = Depends(get_appointment_service),
    patient_service: PatientService = Depends(get_patient_service),
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Create a new appointment.
    """
    try:
        # Get the patient and doctor
        patient = patient_service.get_patient(appointment_data.patient_id)
        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Patient with ID {appointment_data.patient_id} not found"
            )
        
        doctor = doctor_service.get_doctor(appointment_data.doctor_id)
        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Doctor with ID {appointment_data.doctor_id} not found"
            )
        
        # Convert API enum to domain enum
        appointment_type = AppointmentType[appointment_data.type]
        
        # Create the appointment using the factory
        appointment = AppointmentFactory.create_appointment(
            patient=patient,
            doctor=doctor,
            date_time=appointment_data.date_time,
            duration=appointment_data.duration,
            type=appointment_type,
            notes=appointment_data.notes
        )
        
        # Create the appointment using the service
        created_appointment = appointment_service.create_appointment(appointment)
        
        # Convert to response model
        return {
            "id": created_appointment.id,
            "patient_id": created_appointment.patient.id,
            "doctor_id": created_appointment.doctor.id,
            "date_time": created_appointment.date_time,
            "duration": created_appointment.duration,
            "status": created_appointment.status.name,
            "type": created_appointment.type.name,
            "notes": created_appointment.notes
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/appointments", response_model=List[AppointmentResponse])
async def get_all_appointments(
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    """
    Get all appointments.
    """
    appointments = appointment_service.get_all_appointments()
    
    # Convert to response models
    return [
        {
            "id": appointment.id,
            "patient_id": appointment.patient.id,
            "doctor_id": appointment.doctor.id,
            "date_time": appointment.date_time,
            "duration": appointment.duration,
            "status": appointment.status.name,
            "type": appointment.type.name,
            "notes": appointment.notes
        }
        for appointment in appointments
    ]

@router.get("/appointments/{appointment_id}", response_model=AppointmentResponse)
async def get_appointment(
    appointment_id: str,
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    """
    Get an appointment by ID.
    """
    appointment = appointment_service.get_appointment(appointment_id)
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
    
    # Convert to response model
    return {
        "id": appointment.id,
        "patient_id": appointment.patient.id,
        "doctor_id": appointment.doctor.id,
        "date_time": appointment.date_time,
        "duration": appointment.duration,
        "status": appointment.status.name,
        "type": appointment.type.name,
        "notes": appointment.notes
    }

@router.put("/appointments/{appointment_id}", response_model=AppointmentResponse)
async def update_appointment(
    appointment_id: str,
    appointment_data: AppointmentUpdate,
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    """
    Update an appointment.
    """
    try:
        # Get the existing appointment
        existing_appointment = appointment_service.get_appointment(appointment_id)
        if not existing_appointment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Appointment with ID {appointment_id} not found"
            )
        
        # Update the appointment properties
        if appointment_data.date_time:
            existing_appointment.date_time = appointment_data.date_time
        
        if appointment_data.duration:
            existing_appointment.duration = appointment_data.duration
        
        if appointment_data.type:
            existing_appointment.type = AppointmentType[appointment_data.type]
        
        if appointment_data.notes is not None:  # Allow empty string
            existing_appointment.notes = appointment_data.notes
        
        # Update the appointment using the service
        updated_appointment = appointment_service.update_appointment(existing_appointment)
        
        # Convert to response model
        return {
            "id": updated_appointment.id,
            "patient_id": updated_appointment.patient.id,
            "doctor_id": updated_appointment.doctor.id,
            "date_time": updated_appointment.date_time,
            "duration": updated_appointment.duration,
            "status": updated_appointment.status.name,
            "type": updated_appointment.type.name,
            "notes": updated_appointment.notes
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/appointments/{appointment_id}/cancel", response_model=AppointmentResponse)
async def cancel_appointment(
    appointment_id: str,
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    """
    Cancel an appointment.
    """
    try:
        cancelled_appointment = appointment_service.cancel_appointment(appointment_id)
        
        # Convert to response model
        return {
            "id": cancelled_appointment.id,
            "patient_id": cancelled_appointment.patient.id,
            "doctor_id": cancelled_appointment.doctor.id,
            "date_time": cancelled_appointment.date_time,
            "duration": cancelled_appointment.duration,
            "status": cancelled_appointment.status.name,
            "type": cancelled_appointment.type.name,
            "notes": cancelled_appointment.notes
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/appointments/patient/{patient_id}", response_model=List[AppointmentResponse])
async def get_patient_appointments(
    patient_id: str,
    appointment_service: AppointmentService = Depends(get_appointment_service),
    patient_service: PatientService = Depends(get_patient_service)
):
    """
    Get all appointments for a patient.
    """
    # Check if patient exists
    patient = patient_service.get_patient(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    appointments = appointment_service.get_patient_appointments(patient_id)
    
    # Convert to response models
    return [
        {
            "id": appointment.id,
            "patient_id": appointment.patient.id,
            "doctor_id": appointment.doctor.id,
            "date_time": appointment.date_time,
            "duration": appointment.duration,
            "status": appointment.status.name,
            "type": appointment.type.name,
            "notes": appointment.notes
        }
        for appointment in appointments
    ]

@router.get("/appointments/doctor/{doctor_id}", response_model=List[AppointmentResponse])
async def get_doctor_appointments(
    doctor_id: str,
    appointment_service: AppointmentService = Depends(get_appointment_service),
    doctor_service: DoctorService = Depends(get_doctor_service)
):
    """
    Get all appointments for a doctor.
    """
    # Check if doctor exists
    doctor = doctor_service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Doctor with ID {doctor_id} not found"
        )
    
    appointments = appointment_service.get_doctor_appointments(doctor_id)
    
    # Convert to response models
    return [
        {
            "id": appointment.id,
            "patient_id": appointment.patient.id,
            "doctor_id": appointment.doctor.id,
            "date_time": appointment.date_time,
            "duration": appointment.duration,
            "status": appointment.status.name,
            "type": appointment.type.name,
            "notes": appointment.notes
        }
        for appointment in appointments
    ]
