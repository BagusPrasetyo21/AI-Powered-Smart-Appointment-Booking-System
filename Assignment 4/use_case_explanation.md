# Use Case Diagram Explanation

## Key Actors and Their Roles

1. **Patient**
   - Primary user of the appointment booking system
   - Books and manages appointments
   - Provides feedback through ratings and reviews
   - Syncs appointments with personal calendar

2. **Doctor**
   - Healthcare provider managing their schedule
   - Sets availability and working hours
   - Views upcoming appointments
   - Manages calendar synchronization

3. **Admin**
   - System administrator with oversight capabilities
   - Generates and analyzes reports
   - Manages patient data and system configuration
   - Ensures system compliance and security

4. **Receptionist**
   - Front-desk staff assisting with appointments
   - Helps patients with booking process
   - Manages patient records
   - Handles basic system operations

5. **IT Support**
   - Technical team maintaining system health
   - Monitors system performance
   - Handles support tickets
   - Ensures system security and uptime

6. **System**
   - Automated actor handling notifications
   - Sends reminders and confirmations
   - Processes appointment requests
   - Maintains data integrity

## Relationships Between Actors and Use Cases

### Direct Associations
- Actors are connected to use cases they directly interact with using solid lines
- Example: Patient → Book Appointment shows direct interaction

### Include Relationships (<<include>>)
1. **Book Appointment → Send Notifications**
   - Every booking automatically triggers notifications
   - Ensures consistent communication flow

2. **Manage Schedule → Send Notifications**
   - Schedule changes trigger notifications to affected parties
   - Maintains synchronization between doctor and patient schedules

3. **Book Appointment → Manage Patient Data**
   - Booking process requires access to patient records
   - Ensures data consistency and accuracy

### Extend Relationships (<<extend>>)
1. **Rate and Review → Book Appointment**
   - Optional feature available after appointment completion
   - Enhances service quality through feedback

## Addressing Stakeholder Concerns from Assignment 4

1. **Patient Concerns**
   - Easy appointment booking addressed through dedicated "Book Appointment" use case
   - Reminder system implemented via "Send Notifications"
   - Calendar integration through "Sync Calendar" use case
   - Addresses pain points: long waiting times and lack of reminders

2. **Doctor Concerns**
   - Schedule management through "Manage Schedule" use case
   - Notification system reduces no-shows
   - Calendar sync improves time management
   - Addresses pain points: last-minute cancellations and overbooked schedules

3. **Receptionist Concerns**
   - Simplified booking management through shared access to booking system
   - Patient data management streamlined
   - Addresses pain points: tedious manual processes and scheduling errors

4. **Admin Concerns**
   - Comprehensive reporting through "Generate Reports"
   - Patient data management capabilities
   - Addresses pain points: lack of real-time insights

5. **IT Support Concerns**
   - System monitoring capabilities
   - Support ticket management
   - Addresses pain points: system maintenance and security

6. **Regulatory Compliance**
   - Secure patient data management
   - System monitoring for compliance
   - Addresses pain points: data privacy and security requirements

The use case diagram effectively captures the core functionality required by each stakeholder while addressing their specific concerns and pain points identified in Assignment 4. The relationships between use cases demonstrate how the system provides an integrated solution that meets both functional requirements and stakeholder needs.
