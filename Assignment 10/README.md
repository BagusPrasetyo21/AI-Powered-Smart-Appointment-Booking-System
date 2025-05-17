# AI-Powered Smart Appointment Booking System - Implementation

## Project Overview
This repository contains the complete implementation of the AI-Powered Smart Appointment Booking System based on the class diagram developed in [Assessment 9](https://github.com/ncayiyane/Assessment-9.git). The system is designed to streamline appointment booking in healthcare settings using AI to optimize scheduling and improve patient experience.

## Implementation Steps

### 1. Class Implementation (30 Marks)
All classes from the Mermaid.js Class Diagram have been translated into Python code with:

#### Core Classes in `/src` Directory:
- **Patient**: Implemented with private attributes for patient information and methods for booking, canceling, and rescheduling appointments.
- **Doctor**: Implemented with methods to manage availability, view appointments, and access patient records.
- **Appointment**: Central entity with status tracking, confirmation, cancellation, and notification capabilities.
- **Schedule**: Manages doctor availability with working hours and time slot management.
- **TimeSlot**: Represents specific time periods with availability status.
- **Notification**: Handles different types of notifications with delivery status tracking.
- **Rating**: Manages patient feedback on appointments and doctors.
- **MedicalRecord**: Stores patient medical information with diagnoses and medications.
- **Admin**: Provides system administration functionality and reporting.
- **Report**: Handles report generation and formatting with export capabilities.
- **ContactInfo**: Encapsulates contact information for reuse across entities.

#### Enumerations:
- **AppointmentStatus**: SCHEDULED, CONFIRMED, CANCELLED, COMPLETED, NO_SHOW
- **AppointmentType**: REGULAR, FOLLOW_UP, EMERGENCY, CONSULTATION, PROCEDURE
- **NotificationType**: CONFIRMATION, REMINDER, CANCELLATION, RESCHEDULING, GENERAL
- **NotificationStatus**: PENDING, SENT, DELIVERED, READ, FAILED
- **SlotStatus**: AVAILABLE, BOOKED, BLOCKED
- **AdminRole**: SYSTEM_ADMIN, USER_MANAGER, REPORT_ANALYST, SUPPORT_STAFF
- **RecipientType**: PATIENT, DOCTOR, ADMIN
- **ReportType**: APPOINTMENT_SUMMARY, DOCTOR_PERFORMANCE, PATIENT_STATISTICS, SYSTEM_USAGE

#### Implementation Details:
- **Encapsulation**: All attributes are private (prefixed with underscore) with public getter properties.
- **Relationships**: Implemented through composition, association, and aggregation as defined in the class diagram.
- **Method Implementation**: All methods from the class diagram are implemented with appropriate business logic.

### 2. Creational Pattern Implementation (40 Marks)
All six creational design patterns have been implemented in the `/creational_patterns` directory:

#### Simple Factory (`simple_factory.py`)
- **Implementation**: `AppointmentFactory` that creates different types of appointments.
- **Use Case**: Centralizes the creation of appointment objects with different types and durations.
- **Justification**: Used for Appointment creation to hide instantiation logic and provide a consistent interface for creating different appointment types.

#### Factory Method (`factory_method.py`)
- **Implementation**: `NotificationSender` as an abstract class with concrete implementations (Email, SMS, Push).
- **Use Case**: Delegates notification creation to subclasses while maintaining a consistent interface.
- **Justification**: Allows for extensibility in notification delivery mechanisms without changing client code.

#### Abstract Factory (`abstract_factory.py`)
- **Implementation**: `UIFactory` with concrete factories for Web and Mobile platforms.
- **Use Case**: Creates families of related UI components (buttons, text fields) for different platforms.
- **Justification**: Enables the system to support multiple UI platforms while ensuring consistency within each platform.

#### Builder (`builder.py`)
- **Implementation**: `MedicalRecordBuilder` for step-by-step construction of medical records.
- **Use Case**: Constructs complex `MedicalRecord` objects with many optional components.
- **Justification**: Used for MedicalRecord due to its complex nature with many optional fields (diagnoses, medications, allergies, notes).

#### Prototype (`prototype.py`)
- **Implementation**: `TimeSlotPrototype` for cloning existing time slots.
- **Use Case**: Efficiently creates multiple similar time slots without costly initialization.
- **Justification**: Implemented for TimeSlot to efficiently create recurring appointment slots, particularly useful for scheduling patterns.

#### Singleton (`singleton.py`)
- **Implementation**: `SystemConfiguration` and `DatabaseConnection` as thread-safe singletons.
- **Use Case**: Ensures only one instance of system configuration and database connection exists.
- **Justification**: Applied to configuration and database connection to ensure consistent global access points and prevent resource duplication.

### 3. Unit Testing (20 Marks)
Comprehensive unit tests have been implemented in the `/tests` directory:

#### Test Files:
- **test_simple_factory.py**: Tests for appointment creation with different types.
- **test_factory_method.py**: Tests for notification sender implementations.
- **test_abstract_factory.py**: Tests for UI component creation across platforms.
- **test_builder.py**: Tests for step-by-step medical record construction.
- **test_prototype.py**: Tests for time slot cloning and modification.
- **test_singleton.py**: Tests for singleton behavior and thread safety.

#### Testing Coverage:
- **Object Creation**: Tests verify that objects are created correctly with proper initialization.
- **Attribute Initialization**: Tests confirm that all attributes are set correctly.
- **Edge Cases**: Tests handle invalid inputs, thread safety for Singleton, and other edge cases.
- **Behavioral Verification**: Tests ensure that objects behave as expected after creation.

### 4. GitHub Project Updates (10 Marks)
Project tracking and documentation have been updated:

#### CHANGELOG.md:
- Documents all implemented features, design decisions, and technical details.
- Tracks progress on implementation of classes and design patterns.
- Records technical decisions and justifications.

#### README.md:
- Explains language choice and key design decisions.
- Documents project structure and implementation details.
- Provides guidance for getting started with the codebase.

## Language Choice: Python

Python was chosen as the implementation language for this project for the following reasons:

1. **Readability and Maintainability**: Python's clean syntax makes the code more maintainable and easier to understand.

2. **Strong OOP Support**: Python provides robust support for object-oriented programming concepts, including encapsulation, inheritance, and polymorphism.

3. **Type Hinting**: Python's type hinting feature allows for better documentation and IDE support while maintaining flexibility.

4. **Rich Ecosystem**: Python has a vast ecosystem of libraries for data analysis, machine learning, and web frameworks.

5. **Cross-Platform Compatibility**: Python's cross-platform nature ensures the system can run on various operating systems.

## Key Design Decisions

### 1. Encapsulation
- All class attributes are implemented as private (prefixed with underscore) with public getter properties.
- This approach prevents direct manipulation of object state and allows for validation in setter methods.

### 2. Relationship Implementation
- **Composition**: The ContactInfo class is composed within Patient and Doctor classes.
- **Associations**: Relationships between entities are implemented through object references and IDs.
- **One-to-Many Relationships**: Implemented using collections (Lists) where appropriate.

### 3. Enum Usage
- Enumerations are used for status fields and types to ensure type safety and restrict values.
- This approach prevents invalid states and improves code readability.

### 4. Method Implementation
- Methods follow the single responsibility principle, focusing on specific tasks.
- Core business logic is encapsulated within appropriate methods of each class.
- Placeholder implementations are provided where external services would be required.

### 5. Creational Pattern Selection
- **Simple Factory**: Used for Appointment creation to centralize the creation logic.
- **Factory Method**: Implemented for Notifications to support different delivery mechanisms.
- **Abstract Factory**: Applied to UI components to support multiple platforms.
- **Builder**: Used for MedicalRecord due to its complex nature with many optional fields.
- **Prototype**: Implemented for TimeSlot to efficiently create recurring appointment slots.
- **Singleton**: Applied to SystemConfiguration and DatabaseConnection to ensure single instances.

## Project Structure

```
/
├── src/                        # Core class implementations
│   ├── __init__.py
│   ├── admin.py                # Admin class implementation
│   ├── appointment.py          # Appointment class implementation
│   ├── contact_info.py         # ContactInfo class implementation
│   ├── doctor.py               # Doctor class implementation
│   ├── enums.py                # All enumeration types
│   ├── medical_record.py       # MedicalRecord class implementation
│   ├── notification.py         # Notification class implementation
│   ├── patient.py              # Patient class implementation
│   ├── rating.py               # Rating class implementation
│   ├── report.py               # Report class implementation
│   ├── schedule.py             # Schedule class implementation
│   └── time_slot.py            # TimeSlot class implementation
│
├── creational_patterns/        # Creational design patterns
│   ├── __init__.py
│   ├── abstract_factory.py     # Abstract Factory pattern implementation
│   ├── builder.py              # Builder pattern implementation
│   ├── factory_method.py       # Factory Method pattern implementation
│   ├── prototype.py            # Prototype pattern implementation
│   ├── simple_factory.py       # Simple Factory pattern implementation
│   └── singleton.py            # Singleton pattern implementation
│
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_abstract_factory.py
│   ├── test_builder.py
│   ├── test_factory_method.py
│   ├── test_prototype.py
│   ├── test_simple_factory.py
│   └── test_singleton.py
│
├── README.md                   # Project documentation
└── CHANGELOG.md                # Implementation progress tracking
```

## Getting Started

To use this codebase:

1. Clone the repository
   ```
   git clone https://github.com/your-username/appointment-booking-system.git
   ```

2. Ensure Python 3.7+ is installed
   ```
   python --version
   ```

3. Run the unit tests to verify the implementation
   ```
   python -m unittest discover tests
   ```

4. Import the classes in your application
   ```python
   from src.patient import Patient
   from src.doctor import Doctor
   from creational_patterns.simple_factory import AppointmentFactory
   ```

## Related Repositories

- [Assessment 9: Domain Model and Class Diagram](https://github.com/ncayiyane/Assessment-9.git)
- [Assessment 8: Behavioral Models](https://github.com/ncayiyane/Assignment-8.git)
- [Assessment 5 & 6: Use Cases and Agile Planning](https://github.com/ncayiyane/Assignment-5-.git)
- [Assessment 4: Requirements](https://github.com/ncayiyane/AI-Powered-Smart-Appointment-Booking-System-.git)