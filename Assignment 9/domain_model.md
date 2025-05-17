# Domain Model for AI-Powered Smart Appointment Booking System

## Key Domain Entities

| Entity | Attributes | Methods | Relationships | Business Rules |
|--------|------------|---------|---------------|---------------|
| Patient | - patientId: String<br>- name: String<br>- contactInfo: ContactInfo<br>- medicalHistory: List<MedicalRecord><br>- appointmentHistory: List<Appointment> | - bookAppointment()<br>- cancelAppointment()<br>- rescheduleAppointment()<br>- rateAppointment()<br>- syncCalendar()<br>- viewAppointmentHistory() | - Has many Appointments<br>- Has one ContactInfo<br>- Has many MedicalRecords<br>- Creates Ratings | - A patient can have multiple appointments<br>- A patient can only book one appointment for the same time slot<br>- A patient must provide valid contact information for booking |
| Doctor | - doctorId: String<br>- name: String<br>- specialization: String<br>- contactInfo: ContactInfo<br>- schedule: Schedule | - setAvailability()<br>- viewAppointments()<br>- updateSchedule()<br>- accessPatientHistory()<br>- syncCalendar() | - Has many Appointments<br>- Has one Schedule<br>- Has one ContactInfo | - A doctor can only be booked for one appointment per time slot<br>- A doctor must set their availability before appointments can be booked<br>- A doctor can only access patient history for their own patients |
| Appointment | - appointmentId: String<br>- dateTime: DateTime<br>- duration: Integer<br>- status: AppointmentStatus<br>- type: AppointmentType<br>- notes: String | - confirm()<br>- cancel()<br>- reschedule()<br>- sendReminder()<br>- generateNotification() | - Belongs to one Patient<br>- Belongs to one Doctor<br>- May have one Rating<br>- Has one Notification | - Appointments must be booked at least 24 hours in advance<br>- Cancellations must be made at least 6 hours before the appointment<br>- An appointment must have both a patient and a doctor assigned |
| Schedule | - scheduleId: String<br>- workingHours: Map<DayOfWeek, TimeRange><br>- blockedSlots: List<TimeSlot><br>- availableSlots: List<TimeSlot> | - addBlockedTime()<br>- removeBlockedTime()<br>- getAvailableSlots()<br>- checkAvailability() | - Belongs to one Doctor<br>- Contains many TimeSlots | - Working hours must be set within hospital operating hours<br>- Time slots must be at least 15 minutes in duration<br>- Blocked slots cannot be booked |
| Notification | - notificationId: String<br>- type: NotificationType<br>- content: String<br>- timestamp: DateTime<br>- status: NotificationStatus | - send()<br>- markAsRead()<br>- markAsDelivered() | - Associated with one Appointment<br>- Sent to Patient or Doctor | - Appointment reminders must be sent 24 hours before the appointment<br>- Notifications must be sent for all appointment status changes<br>- System must track delivery status of notifications |
| Rating | - ratingId: String<br>- score: Integer (1-5)<br>- comment: String<br>- timestamp: DateTime | - submit()<br>- edit()<br>- delete() | - Created by one Patient<br>- Associated with one Appointment<br>- Associated with one Doctor | - Ratings can only be submitted after an appointment is completed<br>- Ratings can be edited within 48 hours of submission<br>- Rating score must be between 1 and 5 |
| Admin | - adminId: String<br>- name: String<br>- role: AdminRole<br>- permissions: List<Permission> | - generateReports()<br>- manageUsers()<br>- configureSystem()<br>- monitorPerformance() | - Manages Patient accounts<br>- Manages Doctor accounts<br>- Generates Reports | - Admins have different access levels based on their role<br>- Only admins can generate system-wide reports<br>- Admins must log all critical system changes |

## Additional Business Rules

1. **Appointment Booking**:
   - A patient cannot book more than 3 appointments in a single day
   - Appointments must be scheduled during hospital operating hours (8:00 AM - 6:00 PM)
   - Emergency appointments can override normal scheduling rules

2. **Doctor Availability**:
   - Doctors must maintain a minimum of 20 available hours per week
   - Schedule changes must be made at least 48 hours in advance, except for emergencies
   - Doctors cannot be double-booked for appointments

3. **Notification System**:
   - Patients receive appointment confirmations immediately after booking
   - Reminder notifications are sent 24 hours and 1 hour before appointments
   - Both patients and doctors are notified of any schedule changes

4. **Data Management**:
   - Patient medical data must be encrypted at rest and in transit
   - Access to patient data is logged and audited
   - Patient data can only be accessed by authorized personnel

5. **System Performance**:
   - The system must support at least 1000 concurrent users
   - Appointment booking process must complete within 30 seconds
   - System uptime must be maintained at 99.9%
