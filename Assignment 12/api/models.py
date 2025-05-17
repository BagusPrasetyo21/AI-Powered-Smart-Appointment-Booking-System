"""
API models for data validation and serialization.
"""
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enum models
class AppointmentStatusEnum(str, Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    MISSED = "MISSED"

class AppointmentTypeEnum(str, Enum):
    REGULAR = "REGULAR"
    FOLLOW_UP = "FOLLOW_UP"
    EMERGENCY = "EMERGENCY"
    CONSULTATION = "CONSULTATION"

# Contact Info models
class ContactInfoCreate(BaseModel):
    email: EmailStr
    phone: str
    address: str

class ContactInfoResponse(ContactInfoCreate):
    pass

# Patient models
class PatientCreate(BaseModel):
    name: str
    contact_info: ContactInfoCreate

class PatientResponse(BaseModel):
    id: str
    name: str
    contact_info: ContactInfoResponse
    
    class Config:
        schema_extra = {
            "example": {
                "id": "patient-123",
                "name": "John Doe",
                "contact_info": {
                    "email": "john.doe@example.com",
                    "phone": "123-456-7890",
                    "address": "123 Main St, Anytown, USA"
                }
            }
        }

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    contact_info: Optional[ContactInfoCreate] = None

# Doctor models
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    contact_info: ContactInfoCreate

class DoctorResponse(BaseModel):
    id: str
    name: str
    specialization: str
    contact_info: ContactInfoResponse
    
    class Config:
        schema_extra = {
            "example": {
                "id": "doctor-123",
                "name": "Dr. Jane Smith",
                "specialization": "Cardiology",
                "contact_info": {
                    "email": "jane.smith@example.com",
                    "phone": "123-456-7890",
                    "address": "456 Medical Center, Anytown, USA"
                }
            }
        }

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    contact_info: Optional[ContactInfoCreate] = None

# Appointment models
class AppointmentCreate(BaseModel):
    patient_id: str
    doctor_id: str
    date_time: datetime
    duration: int = Field(30, description="Duration in minutes")
    type: AppointmentTypeEnum = AppointmentTypeEnum.REGULAR
    notes: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    date_time: datetime
    duration: int
    status: AppointmentStatusEnum
    type: AppointmentTypeEnum
    notes: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "id": "appointment-123",
                "patient_id": "patient-123",
                "doctor_id": "doctor-123",
                "date_time": "2025-05-10T14:30:00",
                "duration": 30,
                "status": "SCHEDULED",
                "type": "REGULAR",
                "notes": "Regular check-up"
            }
        }

class AppointmentUpdate(BaseModel):
    date_time: Optional[datetime] = None
    duration: Optional[int] = None
    type: Optional[AppointmentTypeEnum] = None
    notes: Optional[str] = None
