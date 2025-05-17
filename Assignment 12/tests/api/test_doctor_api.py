"""
Integration tests for the doctor API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

class TestDoctorAPI:
    """
    Test cases for the doctor API endpoints.
    """
    
    def test_create_doctor(self):
        """Test creating a doctor."""
        # Setup
        doctor_data = {
            "name": "Dr. Jane Smith",
            "specialization": "Cardiology",
            "contact_info": {
                "email": "jane.smith@example.com",
                "phone": "123-456-7890",
                "address": "456 Medical Center, Anytown, USA"
            }
        }
        
        # Execute
        response = client.post("/api/doctors", json=doctor_data)
        
        # Verify
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Dr. Jane Smith"
        assert data["specialization"] == "Cardiology"
        assert data["contact_info"]["email"] == "jane.smith@example.com"
        assert "id" in data
    
    def test_get_all_doctors(self):
        """Test getting all doctors."""
        # Create a doctor first
        doctor_data = {
            "name": "Dr. John Doe",
            "specialization": "Neurology",
            "contact_info": {
                "email": "john.doe@example.com",
                "phone": "123-456-7890",
                "address": "123 Medical Center, Anytown, USA"
            }
        }
        client.post("/api/doctors", json=doctor_data)
        
        # Execute
        response = client.get("/api/doctors")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
    
    def test_get_doctor(self):
        """Test getting a doctor by ID."""
        # Create a doctor first
        doctor_data = {
            "name": "Dr. Bob Johnson",
            "specialization": "Dermatology",
            "contact_info": {
                "email": "bob.johnson@example.com",
                "phone": "123-456-7890",
                "address": "789 Medical Center, Anytown, USA"
            }
        }
        create_response = client.post("/api/doctors", json=doctor_data)
        doctor_id = create_response.json()["id"]
        
        # Execute
        response = client.get(f"/api/doctors/{doctor_id}")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == doctor_id
        assert data["name"] == "Dr. Bob Johnson"
        assert data["specialization"] == "Dermatology"
        assert data["contact_info"]["email"] == "bob.johnson@example.com"
    
    def test_get_doctor_not_found(self):
        """Test getting a non-existent doctor."""
        # Execute
        response = client.get("/api/doctors/non-existent-id")
        
        # Verify
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
    
    def test_update_doctor(self):
        """Test updating a doctor."""
        # Create a doctor first
        doctor_data = {
            "name": "Dr. Alice Brown",
            "specialization": "Pediatrics",
            "contact_info": {
                "email": "alice.brown@example.com",
                "phone": "123-456-7890",
                "address": "101 Medical Center, Anytown, USA"
            }
        }
        create_response = client.post("/api/doctors", json=doctor_data)
        doctor_id = create_response.json()["id"]
        
        # Update data
        update_data = {
            "name": "Dr. Alice Smith",
            "specialization": "Pediatric Cardiology",
            "contact_info": {
                "email": "alice.smith@example.com",
                "phone": "987-654-3210",
                "address": "101 Medical Center, Anytown, USA"
            }
        }
        
        # Execute
        response = client.put(f"/api/doctors/{doctor_id}", json=update_data)
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == doctor_id
        assert data["name"] == "Dr. Alice Smith"
        assert data["specialization"] == "Pediatric Cardiology"
        assert data["contact_info"]["email"] == "alice.smith@example.com"
        assert data["contact_info"]["phone"] == "987-654-3210"
    
    def test_delete_doctor(self):
        """Test deleting a doctor."""
        # Create a doctor first
        doctor_data = {
            "name": "Dr. Charlie Davis",
            "specialization": "Ophthalmology",
            "contact_info": {
                "email": "charlie.davis@example.com",
                "phone": "123-456-7890",
                "address": "202 Medical Center, Anytown, USA"
            }
        }
        create_response = client.post("/api/doctors", json=doctor_data)
        doctor_id = create_response.json()["id"]
        
        # Execute
        response = client.delete(f"/api/doctors/{doctor_id}")
        
        # Verify
        assert response.status_code == 204
        
        # Verify doctor is deleted
        get_response = client.get(f"/api/doctors/{doctor_id}")
        assert get_response.status_code == 404
    
    def test_search_doctors_by_specialization(self):
        """Test searching for doctors by specialization."""
        # Create a doctor first
        doctor_data = {
            "name": "Dr. David Wilson",
            "specialization": "Orthopedics",
            "contact_info": {
                "email": "david.wilson@example.com",
                "phone": "123-456-7890",
                "address": "303 Medical Center, Anytown, USA"
            }
        }
        client.post("/api/doctors", json=doctor_data)
        
        # Execute
        response = client.get("/api/doctors/specialization/Orthopedics")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert any(doctor["specialization"] == "Orthopedics" for doctor in data)
    
    def test_search_doctors_by_name(self):
        """Test searching for doctors by name."""
        # Create a doctor first
        doctor_data = {
            "name": "Dr. Emily Clark",
            "specialization": "Psychiatry",
            "contact_info": {
                "email": "emily.clark@example.com",
                "phone": "123-456-7890",
                "address": "404 Medical Center, Anytown, USA"
            }
        }
        client.post("/api/doctors", json=doctor_data)
        
        # Execute
        response = client.get("/api/doctors/search/Emily")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert any(doctor["name"] == "Dr. Emily Clark" for doctor in data)
