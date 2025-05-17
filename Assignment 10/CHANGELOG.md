# Changelog

## [1.0.0] - 2025-04-18

### Added
- Initial implementation of all core classes from the UML Class Diagram
  - Patient, Doctor, Appointment, Schedule, TimeSlot
  - Notification, Rating, MedicalRecord, Admin, Report
  - ContactInfo and supporting classes
- Implemented all six creational design patterns:
  - Simple Factory: AppointmentFactory for creating different types of appointments
  - Factory Method: NotificationSender hierarchy for creating different notification types
  - Abstract Factory: UIFactory for creating platform-specific UI components
  - Builder: MedicalRecordBuilder for complex medical record creation
  - Prototype: TimeSlotPrototype for efficient time slot creation
  - Singleton: SystemConfiguration and DatabaseConnection for global access points
- Comprehensive unit tests for all creational patterns
  - Tests for correct object creation
  - Tests for proper initialization of attributes
  - Tests for edge cases (thread safety for Singleton, etc.)

### Technical Details
- Chose Python for implementation due to its readability and flexibility
- Organized codebase into three main directories:
  - `/src`: Core class implementations
  - `/creational_patterns`: Specific implementations of all six creational patterns
  - `/tests`: Unit tests for all patterns and core functionality
- Used Python's built-in `unittest` framework for testing
- Implemented proper encapsulation with private attributes and public getters/setters
- Used type hints throughout the codebase for better code readability and IDE support

### Design Decisions
- Used Simple Factory for Appointment creation to centralize the creation logic
- Implemented Factory Method for Notifications to support different delivery mechanisms
- Applied Abstract Factory for UI components to support multiple platforms
- Used Builder for MedicalRecord due to its complex nature with many optional fields
- Implemented Prototype for TimeSlot to efficiently create recurring appointment slots
- Applied Singleton to SystemConfiguration and DatabaseConnection to ensure single instances
