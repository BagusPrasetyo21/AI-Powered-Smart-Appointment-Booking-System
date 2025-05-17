# Assignment 9: Domain Modeling and Class Diagram Development

## Overview
This repository contains the domain model and class diagram for the AI-Powered Smart Appointment Booking System, building upon previous assignments (requirements, use cases, Agile planning, and behavioral models).

## Repository Structure
- [domain_model.md](domain_model.md): Contains the domain model with 7 key entities, their attributes, methods, relationships, and business rules.
- [class_diagram.md](class_diagram.md): Contains a comprehensive class diagram using Mermaid.js syntax that visualizes the system structure.
- [reflection.md](reflection.md): A detailed reflection on the challenges faced, alignment with previous assignments, trade-offs made, and lessons learned.

## Previous Assignments
- [Assignment 4: Requirements](https://github.com/ncayiyane/AI-Powered-Smart-Appointment-Booking-System-.git) - System requirements and stakeholder analysis
- [Assignment 5: Use Cases](https://github.com/ncayiyane/Assignment-5-.git) - Use case modeling and test case development
- [Assignment 6: Agile Planning](https://github.com/ncayiyane/Assignment-5-.git) - User stories, product backlog, and sprint planning
- [Assignment 8: Behavioral Models](https://github.com/ncayiyane/Assignment-8.git) - State and activity diagrams

## Domain Model
The domain model identifies 7 key entities in the AI-Powered Smart Appointment Booking System:
1. Patient
2. Doctor
3. Appointment
4. Schedule
5. Notification
6. Rating
7. Admin

Each entity has defined attributes, methods, relationships, and business rules as detailed in [domain_model.md](domain_model.md).

## Class Diagram
The class diagram visualizes the system structure using Mermaid.js syntax, including:
- Classes with attributes and methods
- Relationships (association, composition)
- Multiplicity (e.g., 1..*, 0..1)
- Enumerations for status fields and types

See [class_diagram.md](class_diagram.md) for the complete diagram and explanation of key design decisions.

## Project Context
The AI-Powered Smart Appointment Booking System is designed to revolutionize how healthcare appointments are managed in hospital settings. This system leverages artificial intelligence to optimize scheduling, reduce wait times, and improve overall patient experience. Key stakeholders include:

- **Patients**: End users who book and manage medical appointments
- **Doctors**: Healthcare providers who manage their schedules and patient appointments
- **Administrators**: Staff who oversee system operations and generate reports
- **Receptionists**: Front-desk staff who assist patients with the booking process
- **IT Support**: Technical team ensuring system functionality and security

## Domain Model Details
The domain model in [domain_model.md](domain_model.md) provides a comprehensive representation of the system's core entities and their interactions. It includes:

### Key Business Rules
- Patients can book multiple appointments but cannot double-book themselves
- Doctors must maintain minimum availability hours and cannot be double-booked
- Appointments require 24-hour advance booking and 6-hour cancellation notice
- Notifications must be sent for all appointment-related events
- Patient data must be securely managed with proper access controls

### Entity Relationships
- **Patient-Appointment**: One-to-many relationship where patients can book multiple appointments
- **Doctor-Appointment**: One-to-many relationship where doctors conduct multiple appointments
- **Doctor-Schedule**: One-to-one relationship where each doctor maintains their own schedule
- **Appointment-Notification**: One-to-many relationship where appointments generate various notifications
- **Patient-Rating**: One-to-many relationship where patients can submit ratings for completed appointments

## Class Diagram Implementation
The class diagram in [class_diagram.md](class_diagram.md) visualizes the object-oriented structure of the system using Mermaid.js. The implementation includes:

### Class Structure
- **Core Classes**: Patient, Doctor, Appointment, Schedule, Notification, Rating, Admin, etc.
- **Supporting Classes**: ContactInfo, MedicalRecord, TimeSlot, Report, etc.
- **Enumerations**: AppointmentStatus, AppointmentType, NotificationType, etc.

### Design Patterns
- **Composition**: Used for complex objects like Schedule containing TimeSlots
- **Aggregation**: Used for relationships like Patient having MedicalRecords
- **Separation of Concerns**: Each class has a clear, single responsibility

### Technical Implementation
The class diagram is implemented using Mermaid.js syntax, which provides a standardized way to represent UML diagrams in Markdown. This approach allows for:
- Clear visualization of class relationships
- Easy maintenance and updates
- Compatibility with GitHub's Markdown rendering

## Reflection Highlights
The reflection in [reflection.md](reflection.md) discusses the challenges and insights gained during the domain modeling and class diagram development process, including:

### Key Challenges
- Determining appropriate abstraction levels
- Defining complex relationships between healthcare entities
- Balancing design purity with practical implementation concerns

### Design Decisions
- Using composition over inheritance for flexibility
- Separating contact information into its own class for reusability
- Implementing a comprehensive notification system for all stakeholders

### Alignment with Previous Work
- How the domain model supports the use cases from Assignment 5
- How the class structure implements the user stories from Assignment 6
- How the behavioral aspects align with the state diagrams from Assignment 8

## Getting Started
To view the domain model and class diagram:
1. Review the domain model in [domain_model.md](domain_model.md)
2. Examine the class diagram in [class_diagram.md](class_diagram.md)
3. Read the reflection on the design process in [reflection.md](reflection.md)

## Future Enhancements
Potential areas for future development include:
- Integration with external calendar systems
- Advanced AI algorithms for optimized scheduling
- Mobile application interfaces for patients and doctors
- Real-time analytics dashboard for administrators
