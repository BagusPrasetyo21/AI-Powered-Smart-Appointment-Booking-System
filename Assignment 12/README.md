# Assignment 12: Service Layer and REST API Implementation

This project implements a service layer and REST API for an AI-Powered Smart Appointment Booking System. It builds upon the domain model (Assignment 9), factories (Assignment 10), and repository layer (Assignment 11) to create a complete application.

## Project Structure

```
Assignment 12/
├── api/                    # REST API implementation
│   ├── routes/             # API route handlers
│   ├── main.py             # Main FastAPI application
│   └── models.py           # API data models
├── docs/                   # API documentation
│   └── openapi.yaml        # OpenAPI specification
├── services/               # Service layer implementation
│   ├── patient_service.py  # Patient business logic
│   ├── doctor_service.py   # Doctor business logic
│   └── appointment_service.py # Appointment business logic
└── tests/                  # Test suite
    ├── api/                # API integration tests
    └── services/           # Service unit tests
```

## Features

### Service Layer
- Implements business logic for patients, doctors, and appointments
- Validates inputs and enforces business rules
- Uses repositories for data persistence
- Includes comprehensive unit tests

### REST API
- RESTful endpoints for CRUD operations
- Business workflow endpoints (e.g., cancel appointment)
- Input validation using Pydantic models
- Proper error handling and status codes
- Integration tests for all endpoints

### API Documentation
- OpenAPI/Swagger documentation
- Endpoint descriptions
- Request/response schemas
- Error responses

## API Endpoints

### Patients
- `GET /api/patients` - Get all patients
- `POST /api/patients` - Create a new patient
- `GET /api/patients/{patient_id}` - Get a patient by ID
- `PUT /api/patients/{patient_id}` - Update a patient
- `DELETE /api/patients/{patient_id}` - Delete a patient
- `GET /api/patients/search/{name}` - Search for patients by name

### Doctors
- `GET /api/doctors` - Get all doctors
- `POST /api/doctors` - Create a new doctor
- `GET /api/doctors/{doctor_id}` - Get a doctor by ID
- `PUT /api/doctors/{doctor_id}` - Update a doctor
- `DELETE /api/doctors/{doctor_id}` - Delete a doctor
- `GET /api/doctors/specialization/{specialization}` - Search for doctors by specialization
- `GET /api/doctors/search/{name}` - Search for doctors by name

### Appointments
- `GET /api/appointments` - Get all appointments
- `POST /api/appointments` - Create a new appointment
- `GET /api/appointments/{appointment_id}` - Get an appointment by ID
- `PUT /api/appointments/{appointment_id}` - Update an appointment
- `POST /api/appointments/{appointment_id}/cancel` - Cancel an appointment
- `GET /api/appointments/patient/{patient_id}` - Get all appointments for a patient
- `GET /api/appointments/doctor/{doctor_id}` - Get all appointments for a doctor

## Business Rules

The service layer enforces several business rules, including:
- Patients can't book more than 3 appointments in a single day
- Appointments must be booked at least 24 hours in advance
- Cancellations must be made at least 6 hours before the appointment
- Doctors cannot be double-booked for appointments

## Installation and Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   uvicorn api.main:app --reload
   ```
4. Access the API documentation at http://localhost:8000/docs

## Testing

### Running Tests Locally

Run the tests using pytest:
```
pytest
```

To run specific test files:
```
pytest tests/api/test_patient_api.py
pytest tests/services/test_appointment_service.py
```

To run tests with verbose output:
```
pytest -v
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and continuous deployment.

### CI Pipeline

The CI pipeline runs automatically on:
- Every push to any branch
- Every pull request to the main branch

The CI pipeline:
1. Sets up a Python environment
2. Installs all dependencies
3. Runs all tests using pytest
4. Blocks PR merges if tests fail

### CD Pipeline

The CD pipeline runs automatically when code is merged to the main branch and:
1. Builds a Python package artifact
2. Uploads the artifact to GitHub Actions

### Branch Protection

The main branch is protected with the following rules:
- Requires at least one pull request review
- Requires all status checks (tests) to pass
- Prevents direct pushes (all changes must go through PRs)

See [PROTECTION.md](PROTECTION.md) for details on why these rules are important.

## Future Improvements

- Add authentication and authorization
- Implement email notifications for appointments
- Add support for recurring appointments
- Create a web or mobile frontend
- Add code coverage reporting to CI pipeline
- Implement automatic deployment to a cloud provider
