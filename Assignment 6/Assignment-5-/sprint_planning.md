# Sprint Planning

## Sprint Goal
Implement the core appointment booking functionality that allows patients to schedule appointments and doctors to manage their availability, creating a minimum viable product (MVP) that addresses the primary needs of both patients and healthcare providers.

## Sprint Duration
2 weeks (10 working days)

## Selected User Stories for Sprint 1

| Story ID | User Story | Priority (MoSCoW) | Effort Estimate | 
|----------|------------|-------------------|-----------------|
| US-001 | As a patient, I want to book appointments online so that I can schedule medical visits without making phone calls. | Must-have | 5 |
| US-005 | As a doctor, I want to set my availability schedule so that patients can only book during my working hours. | Must-have | 4 |
| US-006 | As a doctor, I want to view my upcoming appointments so that I can prepare for patient visits. | Must-have | 3 |
| US-002 | As a patient, I want to receive appointment reminders so that I don't forget my scheduled visits. | Must-have | 3 |
| US-013 | As a system administrator, I want patient data to be encrypted so that security compliance requirements are met. | Must-have | 5 |

Total Story Points: 20

## Sprint Backlog Tasks

| Task ID | Task Description | Assigned To | Estimated Hours | Status |
|---------|------------------|-------------|-----------------|--------|
| T-001 | Design database schema for appointments and user profiles | Database Team | 8 | To Do |
| T-002 | Develop API endpoint for appointment creation | Backend Team | 10 | To Do |
| T-003 | Implement doctor availability management interface | Frontend Team | 12 | To Do |
| T-004 | Create patient appointment booking UI | Frontend Team | 16 | To Do |
| T-005 | Implement data encryption for patient records | Security Team | 10 | To Do |
| T-006 | Develop appointment reminder notification system | Backend Team | 8 | To Do |
| T-007 | Create doctor's appointment dashboard | Frontend Team | 12 | To Do |
| T-008 | Implement authentication and authorization system | Security Team | 14 | To Do |
| T-009 | Design and implement API for doctor availability | Backend Team | 10 | To Do |
| T-010 | Create unit tests for booking functionality | QA Team | 8 | To Do |
| T-011 | Create integration tests for appointment flow | QA Team | 8 | To Do |
| T-012 | Implement logging system for security auditing | Security Team | 6 | To Do |
| T-013 | Create deployment pipeline for staging environment | DevOps Team | 8 | To Do |
| T-014 | Conduct security review of encryption implementation | Security Team | 6 | To Do |
| T-015 | Implement responsive design for mobile devices | Frontend Team | 10 | To Do |

Total Estimated Hours: 146

## Sprint Capacity
- 5 developers × 6 productive hours/day × 10 days = 300 hours
- Accounting for meetings, code reviews, and other activities: 300 × 0.7 = 210 available hours
- Sprint backlog requires 146 hours, which is within our capacity with buffer for unexpected issues

## MVP Contribution
This sprint delivers the core functionality needed for a viable appointment booking system:

1. **Patient-facing features:**
   - Online appointment booking
   - Appointment reminders

2. **Doctor-facing features:**
   - Availability management
   - Appointment dashboard

3. **System requirements:**
   - Data security and encryption

These features address the most critical pain points identified in previous assignments:
- Patients: Difficulty scheduling appointments and forgetting appointments
- Doctors: Managing availability and preparing for patient visits
- System: Meeting security and compliance requirements

Subsequent sprints will build upon this foundation to add additional features like calendar synchronization, reporting, and review capabilities.
