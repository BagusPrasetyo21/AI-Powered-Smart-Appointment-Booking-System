"""
Integration tests for the appointment API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from api.main import app

client = TestClient(app)

class TestAppointmentAPI:
    """
    Test cases for the appointment API endpoints.
    """
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Create a patient
        patient_data = {
            "name": "Test Patient",
            "contact_info": {
                "email": "test.patient@example.com",
                "phone": "123-456-7890",
                "address": "123 Test St, Anytown, USA"
            }
        }
        patient_response = client.post("/api/patients", json=patient_data)
        self.patient_id = patient_response.json()["id"]
        
        # Create a doctor
        doctor_data = {
            "name": "Dr. Test Doctor",
            "specialization": "General Medicine",
            "contact_info": {
                "email": "test.doctor@example.com",
                "phone": "123-456-7890",
                "address": "456 Test Medical Center, Anytown, USA"
            }
        }
        doctor_response = client.post("/api/doctors", json=doctor_data)
        self.doctor_id = doctor_response.json()["id"]
    
    def test_create_appointment(self):
        """Test creating an appointment."""
        # Setup
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        
        # Execute
        response = client.post("/api/appointments", json=appointment_data)
        
        # Verify
        assert response.status_code == 201
        data = response.json()
        assert data["patient_id"] == self.patient_id
        assert data["doctor_id"] == self.doctor_id
        assert data["status"] == "SCHEDULED"
        assert data["type"] == "REGULAR"
        assert data["notes"] == "Regular check-up"
        assert "id" in data
    
    def test_get_all_appointments(self):
        """Test getting all appointments."""
        # Create an appointment first
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        client.post("/api/appointments", json=appointment_data)
        
        # Execute
        response = client.get("/api/appointments")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
    
    def test_get_appointment(self):
        """Test getting an appointment by ID."""
        # Create an appointment first
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        create_response = client.post("/api/appointments", json=appointment_data)
        appointment_id = create_response.json()["id"]
        
        # Execute
        response = client.get(f"/api/appointments/{appointment_id}")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == appointment_id
        assert data["patient_id"] == self.patient_id
        assert data["doctor_id"] == self.doctor_id
        assert data["status"] == "SCHEDULED"
    
    def test_get_appointment_not_found(self):
        """Test getting a non-existent appointment."""
        # Execute
        response = client.get("/api/appointments/non-existent-id")
        
        # Verify
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
    
    def test_update_appointment(self):
        """Test updating an appointment."""
        # Create an appointment first
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        create_response = client.post("/api/appointments", json=appointment_data)
        appointment_id = create_response.json()["id"]
        
        # Update data
        new_time = datetime.now() + timedelta(days=4)
        update_data = {
            "date_time": new_time.isoformat(),
            "duration": 45,
            "type": "FOLLOW_UP",
            "notes": "Follow-up appointment"
        }
        
        # Execute
        response = client.put(f"/api/appointments/{appointment_id}", json=update_data)
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == appointment_id
        assert data["duration"] == 45
        assert data["type"] == "FOLLOW_UP"
        assert data["notes"] == "Follow-up appointment"
    
    def test_cancel_appointment(self):
        """Test cancelling an appointment."""
        # Create an appointment first
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        create_response = client.post("/api/appointments", json=appointment_data)
        appointment_id = create_response.json()["id"]
        
        # Execute
        response = client.post(f"/api/appointments/{appointment_id}/cancel")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == appointment_id
        assert data["status"] == "CANCELLED"
    
    def test_get_patient_appointments(self):
        """Test getting all appointments for a patient."""
        # Create an appointment first
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        client.post("/api/appointments", json=appointment_data)
        
        # Execute
        response = client.get(f"/api/appointments/patient/{self.patient_id}")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert all(appointment["patient_id"] == self.patient_id for appointment in data)
    
    def test_get_doctor_appointments(self):
        """Test getting all appointments for a doctor."""
        # Create an appointment first
        appointment_time = datetime.now() + timedelta(days=3)
        appointment_data = {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_time": appointment_time.isoformat(),
            "duration": 30,
            "type": "REGULAR",
            "notes": "Regular check-up"
        }
        client.post("/api/appointments", json=appointment_data)
        
        # Execute
        response = client.get(f"/api/appointments/doctor/{self.doctor_id}")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert all(appointment["doctor_id"] == self.doctor_id for appointment in data)
