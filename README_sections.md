# AI-Powered Smart Appointment Booking System

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Updated](https://img.shields.io/badge/last%20updated-May%202025-orange)

An intelligent, AI-driven medical appointment booking system designed to streamline scheduling for healthcare providers and patients. By leveraging artificial intelligence, the system optimizes appointment allocations based on availability, urgency, and patient preferences.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Core Features](#core-features)
- [Technology Stack](#technology-stack)
- [Installation & Setup](#installation--setup)
- [API Documentation](#api-documentation)
- [Future Development](#future-development)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Project Overview

The AI-Powered Smart Appointment Booking System addresses common challenges in medical appointment scheduling:

- **Inefficient Manual Scheduling**: Eliminates the need for patients to manually search for available time slots
- **Schedule Optimization**: Reduces gaps and overbookings in doctor schedules
- **Intelligent Allocation**: Adapts to patient preferences and appointment urgency
- **Administrative Efficiency**: Reduces staff workload for managing appointments

This project is structured as a series of educational assignments that collectively build a comprehensive medical appointment booking system with AI-driven scheduling capabilities.

## 📁 Project Structure

The project is organized into multiple assignments, each focusing on different aspects of the system:

### Assignment 3: Initial Architecture
- System architecture documentation
- High-level specifications
- Initial requirements

### Assignment 4: Use Case Design
- Detailed use case diagrams
- Use case specifications
- Initial test cases

### Assignment 5: Refined Design
- Final use case diagrams
- Comprehensive test cases
- Documentation updates

### Assignment 8: Activity Diagrams
- Workflow visualizations
- Process flows
- System monitoring workflows

### Assignment 11: Core Implementation
- Domain models implementation
- Key classes:
  - `Appointment`: Manages appointment data and status
  - `Doctor`: Handles doctor information and availability
  - `Patient`: Manages patient data and appointment booking
  - `Schedule`: Controls time slot management
  - `Notification`: Handles appointment reminders and alerts
  - `MedicalRecord`: Stores patient medical information

### Assignment 12: API Implementation
- FastAPI application
- RESTful endpoints
- Service layer implementation
- Repository pattern for data access

### Assignment 14: Project Roadmap
- Future development plans
- Feature expansion timeline
- Contribution guidelines

## 🚀 Core Features

### Appointment Management
- Create, view, update, and cancel appointments
- Appointment status tracking (scheduled, confirmed, cancelled, completed)
- Appointment type classification (regular, follow-up, emergency, consultation, procedure)

### Doctor Management
- Doctor profiles with specializations
- Schedule management and availability settings
- Patient history access

### Patient Management
- Patient registration and profiles
- Appointment booking and management
- Medical history tracking

### Scheduling System
- Time slot management
- Availability checking
- Schedule optimization

### Notification System
- Appointment confirmations
- Reminders
- Cancellation notices
- Rescheduling alerts

### Admin Dashboard
- User management
- Appointment oversight
- System configuration

## 💻 Technology Stack

### Backend
- **Language**: Python
- **API Framework**: FastAPI
- **Data Storage**: Repository pattern with in-memory implementation (expandable to databases)
- **Authentication**: JWT (planned/in progress)

### Architecture
- **Design Pattern**: Repository pattern for data access
- **Service Layer**: Business logic encapsulation
- **Domain-Driven Design**: Focus on medical appointment domain

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/ncayiyane/AI-Powered-Smart-Appointment-Booking-System.git
cd AI-Powered-Smart-Appointment-Booking-System
```

2. **Set up a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies for Assignment 12 API**
```bash
cd "Assignment 12"
pip install fastapi uvicorn
# Additional dependencies may be required
```

4. **Run the FastAPI application**
```bash
uvicorn api.main:app --reload
```

5. **Access the API documentation**
```
http://localhost:8000/docs
```

## 📚 API Documentation

The system exposes RESTful APIs through FastAPI:

### Patient Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/patients` | GET | Get all patients |
| `/api/patients/{id}` | GET | Get patient by ID |
| `/api/patients` | POST | Create new patient |
| `/api/patients/{id}` | PUT | Update patient |
| `/api/patients/{id}` | DELETE | Delete patient |

### Doctor Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/doctors` | GET | Get all doctors |
| `/api/doctors/{id}` | GET | Get doctor by ID |
| `/api/doctors` | POST | Create new doctor |
| `/api/doctors/{id}` | PUT | Update doctor |
| `/api/doctors/{id}` | DELETE | Delete doctor |

### Appointment Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/appointments` | GET | Get all appointments |
| `/api/appointments/{id}` | GET | Get appointment by ID |
| `/api/appointments` | POST | Create new appointment |
| `/api/appointments/{id}` | PUT | Update appointment |
| `/api/appointments/{id}` | DELETE | Cancel appointment |
| `/api/appointments/patient/{patient_id}` | GET | Get patient's appointments |
| `/api/appointments/doctor/{doctor_id}` | GET | Get doctor's appointments |

## 🧠 AI Scheduling Logic (Planned Implementation)

The system is designed to incorporate AI-driven scheduling with these components:

1. **Patient Preference Analysis**
   - Track historical booking patterns
   - Identify preferred days, times, and doctors

2. **Urgency Classification**
   - Categorize appointments based on type and urgency
   - Prioritize time-sensitive appointments

3. **Availability Optimization**
   - Maintain real-time availability data
   - Prevent scheduling conflicts

4. **Recommendation Engine**
   - Suggest optimal time slots based on multiple factors
   - Continuously improve through feedback

5. **Load Balancing**
   - Distribute appointments among doctors
   - Consider specialization and workload

## 🔮 Future Development

### Short-term Goals
- Complete AI scheduling algorithm implementation
- Add database persistence layer
- Implement authentication and authorization
- Develop frontend user interface

### Mid-term Goals
- Enhanced notification system with email/SMS
- Patient portal for self-service
- Doctor mobile application
- Reporting and analytics dashboard

### Long-term Vision
- Integration with hospital management systems
- Predictive analytics for resource planning
- Telemedicine integration
- Advanced AI for medical decision support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

© 2025 AI-Powered Smart Appointment Booking System. All rights reserved.
