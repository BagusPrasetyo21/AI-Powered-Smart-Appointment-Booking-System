# Integration with Prior Work

This document maps the state transition diagrams and activity diagrams to the functional requirements from Assignment 4, user stories from Assignment 5, and sprint tasks from Assignment 6, demonstrating the traceability and integration of our modeling work with previous assignments.

## State Diagram Traceability

### 1. Appointment State Diagram

| State/Transition | Functional Requirement | User Story | Sprint Task |
|------------------|------------------------|------------|-------------|
| Requested → Scheduled | FR-001: Allow patients to book appointments online | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-002: Develop API endpoint for appointment creation |
| Scheduled → Rescheduled | FR-003: Allow patients to reschedule appointments | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-004: Create patient appointment booking UI |
| Scheduled → Canceled | FR-004: Allow patients to cancel appointments | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-004: Create patient appointment booking UI |
| CheckedIn → InProgress → Completed | FR-009: Allow doctors to update appointment status | US-006: As a doctor, I want to view my upcoming appointments so that I can prepare for patient visits | T-007: Create doctor's appointment dashboard |
| Completed → Reviewed | FR-012: Allow patients to rate and review appointments | US-004: As a patient, I want to rate and review my appointments so that I can provide feedback on my experience | Not in Sprint 1 |

### 2. User Account State Diagram

| State/Transition | Functional Requirement | User Story | Sprint Task |
|------------------|------------------------|------------|-------------|
| Registered → PendingVerification → Active | FR-002: Require patient registration before booking | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-008: Implement authentication and authorization system |
| Active → Locked | FR-023: Implement account security measures | US-011: As an admin, I want to manage user accounts so that I can control system access and permissions | T-008: Implement authentication and authorization system |
| Active → Suspended | FR-024: Allow administrators to manage user accounts | US-011: As an admin, I want to manage user accounts so that I can control system access and permissions | T-008: Implement authentication and authorization system |
| Deactivated → Deleted | FR-025: Comply with data retention policies | US-013: As a system administrator, I want patient data to be encrypted so that security compliance requirements are met | T-005: Implement data encryption for patient records |

### 3. Doctor Availability State Diagram

| State/Transition | Functional Requirement | User Story | Sprint Task |
|------------------|------------------------|------------|-------------|
| Created → Available | FR-006: Allow doctors to set availability | US-005: As a doctor, I want to set my availability schedule so that patients can only book during my working hours | T-003: Implement doctor availability management interface |
| Available → Reserved → Confirmed | FR-001: Allow patients to book appointments online | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-002: Develop API endpoint for appointment creation |
| Available → Blocked | FR-007: Allow doctors to block time slots | US-005: As a doctor, I want to set my availability schedule so that patients can only book during my working hours | T-009: Design and implement API for doctor availability |
| Confirmed → NoShow | FR-010: Track no-show appointments | US-006: As a doctor, I want to view my upcoming appointments so that I can prepare for patient visits | T-007: Create doctor's appointment dashboard |

### 4. Patient Record State Diagram

| State/Transition | Functional Requirement | User Story | Sprint Task |
|------------------|------------------------|------------|-------------|
| Created → Incomplete → Complete | FR-013: Collect comprehensive patient information | US-009: As a receptionist, I want to update patient information so that records remain accurate and current | Not in Sprint 1 |
| Complete → Active | FR-014: Validate patient information | US-009: As a receptionist, I want to update patient information so that records remain accurate and current | Not in Sprint 1 |
| Active → Updated | FR-015: Allow updating of patient records | US-009: As a receptionist, I want to update patient information so that records remain accurate and current | Not in Sprint 1 |
| Active → Locked | FR-016: Protect sensitive patient information | US-013: As a system administrator, I want patient data to be encrypted so that security compliance requirements are met | T-005: Implement data encryption for patient records |

### 5. Notification State Diagram

| State/Transition | Functional Requirement | User Story | Sprint Task |
|------------------|------------------------|------------|-------------|
| Created → Queued → Sent | FR-019: Generate automated notifications | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Sent → Delivered → Read | FR-020: Track notification delivery status | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Sent → Failed → Retrying | FR-021: Handle failed notification delivery | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Delivered → Acknowledged | FR-022: Track user response to notifications | US-007: As a doctor, I want to receive notifications about schedule changes so that I'm aware of cancellations or new bookings | Not in Sprint 1 |

## Activity Diagram Traceability

### 1. Appointment Booking Workflow

| Activity/Decision | Functional Requirement | User Story | Sprint Task |
|-------------------|------------------------|------------|-------------|
| Patient logs in to system | FR-002: Require patient registration before booking | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-008: Implement authentication and authorization system |
| View available time slots | FR-006: Allow doctors to set availability | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-004: Create patient appointment booking UI |
| Validate request | FR-005: Prevent double-booking of appointments | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-002: Develop API endpoint for appointment creation |
| Send confirmation to patient | FR-019: Generate automated notifications | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Sync with external calendars | FR-045: Support calendar synchronization | US-003: As a patient, I want to sync appointments with my personal calendar so that I can manage all my schedules in one place | Not in Sprint 1 |

### 2. Doctor Availability Management Workflow

| Activity/Decision | Functional Requirement | User Story | Sprint Task |
|-------------------|------------------------|------------|-------------|
| Set recurring availability pattern | FR-006: Allow doctors to set availability | US-005: As a doctor, I want to set my availability schedule so that patients can only book during my working hours | T-003: Implement doctor availability management interface |
| Block time slot | FR-007: Allow doctors to block time slots | US-005: As a doctor, I want to set my availability schedule so that patients can only book during my working hours | T-009: Design and implement API for doctor availability |
| Handle existing appointments | FR-046: Manage appointment conflicts | US-007: As a doctor, I want to receive notifications about schedule changes so that I'm aware of cancellations or new bookings | Not in Sprint 1 |
| Notify about schedule change | FR-019: Generate automated notifications | US-007: As a doctor, I want to receive notifications about schedule changes so that I'm aware of cancellations or new bookings | Not in Sprint 1 |

### 3. Appointment Reminder Workflow

| Activity/Decision | Functional Requirement | User Story | Sprint Task |
|-------------------|------------------------|------------|-------------|
| Query upcoming appointments | FR-019: Generate automated notifications | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Check patient notification preferences | FR-047: Respect user communication preferences | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Send email/SMS/app notification | FR-019: Generate automated notifications | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Track reminder status | FR-020: Track notification delivery status | US-002: As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits | T-006: Develop appointment reminder notification system |
| Trigger reschedule/cancellation workflow | FR-003/FR-004: Allow patients to reschedule/cancel appointments | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-004: Create patient appointment booking UI |

### 4. Patient Registration Workflow

| Activity/Decision | Functional Requirement | User Story | Sprint Task |
|-------------------|------------------------|------------|-------------|
| Enter basic personal information | FR-013: Collect comprehensive patient information | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-001: Design database schema for appointments and user profiles |
| Validate all inputs | FR-014: Validate patient information | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-002: Develop API endpoint for appointment creation |
| Send verification email | FR-026: Verify user email addresses | US-011: As an admin, I want to manage user accounts so that I can control system access and permissions | T-008: Implement authentication and authorization system |
| Create patient record | FR-013: Collect comprehensive patient information | US-001: As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls | T-001: Design database schema for appointments and user profiles |

## Summary of Integration

The state transition diagrams and activity diagrams provide a comprehensive view of the dynamic behavior of our AI-Powered Smart Appointment Booking System. These diagrams directly build upon:

1. **Functional Requirements (Assignment 4)**: Each state and transition maps to specific functional requirements, ensuring that our system behavior models align with the specified system capabilities.

2. **User Stories (Assignment 5)**: The diagrams illustrate how the system fulfills user stories by modeling the interactions and workflows from the perspective of different stakeholders (patients, doctors, staff, administrators).

3. **Sprint Tasks (Assignment 6)**: Many of the states and activities connect to specific implementation tasks from our first sprint plan, showing how the modeled behavior will be realized in the actual system.

This integration ensures that our system modeling is not just theoretical but directly applicable to the implementation work planned in our Agile development process. The diagrams serve as a bridge between requirements and implementation, providing a clear blueprint for developers to follow.
