"""
Main FastAPI application for the AI-Powered Smart Appointment Booking System.
"""
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from typing import List, Optional

# Import models and services
from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment
from src.enums import AppointmentStatus

# Import repositories
from repositories.inmemory.inmemory_patient_repository import InMemoryPatientRepository
from repositories.inmemory.inmemory_doctor_repository import InMemoryDoctorRepository
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository

# Import services
from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.appointment_service import AppointmentService

# Import API models
from api.models import (
    PatientCreate, PatientResponse, PatientUpdate,
    DoctorCreate, DoctorResponse, DoctorUpdate,
    AppointmentCreate, AppointmentResponse, AppointmentUpdate
)

# Create FastAPI app
app = FastAPI(
    title="AI-Powered Smart Appointment Booking System",
    description="REST API for managing patients, doctors, and appointments",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create repositories
patient_repository = InMemoryPatientRepository()
doctor_repository = InMemoryDoctorRepository()
appointment_repository = InMemoryAppointmentRepository()

# Create services
patient_service = PatientService(patient_repository)
doctor_service = DoctorService(doctor_repository)
appointment_service = AppointmentService(
    appointment_repository,
    patient_repository,
    doctor_repository
)

# Dependency to get services
def get_patient_service():
    return patient_service

def get_doctor_service():
    return doctor_service

def get_appointment_service():
    return appointment_service

# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    # Add custom components or modify schema here if needed
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the AI-Powered Smart Appointment Booking System API"}

# Include routers
from api.routes.patient_routes import router as patient_router
from api.routes.doctor_routes import router as doctor_router
from api.routes.appointment_routes import router as appointment_router

app.include_router(patient_router, prefix="/api", tags=["Patients"])
app.include_router(doctor_router, prefix="/api", tags=["Doctors"])
app.include_router(appointment_router, prefix="/api", tags=["Appointments"])

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
