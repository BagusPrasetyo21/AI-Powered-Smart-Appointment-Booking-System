"""
Integration tests for the patient API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

class TestPatientAPI:
    """
    Test cases for the patient API endpoints.
    """
    
    def test_create_patient(self):
        """Test creating a patient."""
        # Setup
        patient_data = {
            "name": "John Doe",
            "contact_info": {
                "email": "john.doe@example.com",
                "phone": "123-456-7890",
                "address": "123 Main St, Anytown, USA"
            }
        }
        
        # Execute
        response = client.post("/api/patients", json=patient_data)
        
        # Verify
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John Doe"
        assert data["contact_info"]["email"] == "john.doe@example.com"
        assert "id" in data
    
    def test_get_all_patients(self):
        """Test getting all patients."""
        # Create a patient first
        patient_data = {
            "name": "Jane Smith",
            "contact_info": {
                "email": "jane.smith@example.com",
                "phone": "123-456-7890",
                "address": "456 Oak St, Anytown, USA"
            }
        }
        client.post("/api/patients", json=patient_data)
        
        # Execute
        response = client.get("/api/patients")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
    
    def test_get_patient(self):
        """Test getting a patient by ID."""
        # Create a patient first
        patient_data = {
            "name": "Bob Johnson",
            "contact_info": {
                "email": "bob.johnson@example.com",
                "phone": "123-456-7890",
                "address": "789 Pine St, Anytown, USA"
            }
        }
        create_response = client.post("/api/patients", json=patient_data)
        patient_id = create_response.json()["id"]
        
        # Execute
        response = client.get(f"/api/patients/{patient_id}")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == patient_id
        assert data["name"] == "Bob Johnson"
        assert data["contact_info"]["email"] == "bob.johnson@example.com"
    
    def test_get_patient_not_found(self):
        """Test getting a non-existent patient."""
        # Execute
        response = client.get("/api/patients/non-existent-id")
        
        # Verify
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
    
    def test_update_patient(self):
        """Test updating a patient."""
        # Create a patient first
        patient_data = {
            "name": "Alice Brown",
            "contact_info": {
                "email": "alice.brown@example.com",
                "phone": "123-456-7890",
                "address": "101 Elm St, Anytown, USA"
            }
        }
        create_response = client.post("/api/patients", json=patient_data)
        patient_id = create_response.json()["id"]
        
        # Update data
        update_data = {
            "name": "Alice Smith",
            "contact_info": {
                "email": "alice.smith@example.com",
                "phone": "987-654-3210",
                "address": "101 Elm St, Anytown, USA"
            }
        }
        
        # Execute
        response = client.put(f"/api/patients/{patient_id}", json=update_data)
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == patient_id
        assert data["name"] == "Alice Smith"
        assert data["contact_info"]["email"] == "alice.smith@example.com"
        assert data["contact_info"]["phone"] == "987-654-3210"
    
    def test_delete_patient(self):
        """Test deleting a patient."""
        # Create a patient first
        patient_data = {
            "name": "Charlie Davis",
            "contact_info": {
                "email": "charlie.davis@example.com",
                "phone": "123-456-7890",
                "address": "202 Maple St, Anytown, USA"
            }
        }
        create_response = client.post("/api/patients", json=patient_data)
        patient_id = create_response.json()["id"]
        
        # Execute
        response = client.delete(f"/api/patients/{patient_id}")
        
        # Verify
        assert response.status_code == 204
        
        # Verify patient is deleted
        get_response = client.get(f"/api/patients/{patient_id}")
        assert get_response.status_code == 404
    
    def test_search_patients_by_name(self):
        """Test searching for patients by name."""
        # Create a patient first
        patient_data = {
            "name": "David Wilson",
            "contact_info": {
                "email": "david.wilson@example.com",
                "phone": "123-456-7890",
                "address": "303 Cedar St, Anytown, USA"
            }
        }
        client.post("/api/patients", json=patient_data)
        
        # Execute
        response = client.get("/api/patients/search/David")
        
        # Verify
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert any(patient["name"] == "David Wilson" for patient in data)
