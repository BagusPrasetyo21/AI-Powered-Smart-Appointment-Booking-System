# Use Case Specifications

## 1. Book Appointment (UC2)
**Actor:** Patient, Receptionist
**Description:** Allows patients or receptionists to book medical appointments
**Preconditions:** 
- User is logged in
- Doctor availability is up to date

**Basic Flow:**
1. User selects "Book Appointment" option
2. System displays available doctors and time slots
3. User selects preferred doctor and time slot
4. System validates the selection
5. User confirms booking
6. System creates appointment and sends confirmation

**Alternative Flows:**
- A1: Selected time slot becomes unavailable
  1. System notifies user of unavailability
  2. Returns to step 2
- A2: Doctor cancels availability
  1. System notifies affected patients
  2. Offers rebooking options

**Postconditions:**
- Appointment is created
- Confirmation sent to patient
- Doctor's schedule updated

## 2. Manage Schedule (UC3)
**Actor:** Doctor
**Description:** Allows doctors to manage their availability
**Preconditions:** Doctor is logged in

**Basic Flow:**
1. Doctor accesses schedule management
2. System displays current schedule
3. Doctor adds/modifies available time slots
4. System validates changes
5. System updates availability

**Alternative Flows:**
- A1: Conflict with existing appointments
  1. System shows conflicting appointments
  2. Doctor must resolve conflicts first

**Postconditions:**
- Schedule updated
- Affected appointments notified

## 3. Send Notifications (UC4)
**Actor:** System
**Description:** Automated sending of notifications and reminders
**Preconditions:** Valid appointment exists

**Basic Flow:**
1. System checks upcoming appointments
2. Generates appropriate notification
3. Sends via email/SMS
4. Records notification status

**Alternative Flows:**
- A1: Delivery failure
  1. System retries delivery
  2. Logs failure after 3 attempts

**Postconditions:**
- Notification sent and logged
- Delivery status recorded

## 4. Generate Reports (UC5)
**Actor:** Admin
**Description:** Generate system analytics and reports
**Preconditions:** Admin is logged in

**Basic Flow:**
1. Admin selects report type
2. Specifies time period
3. System generates report
4. Admin views/downloads report

**Alternative Flows:**
- A1: No data available
  1. System shows "No data" message
  2. Suggests different parameters

**Postconditions:**
- Report generated
- Data analysis completed

## 5. Manage Patient Data (UC6)
**Actor:** Admin, Receptionist
**Description:** Manage patient records and information
**Preconditions:** User has appropriate permissions

**Basic Flow:**
1. User searches for patient record
2. System displays patient information
3. User makes necessary updates
4. System validates changes
5. System saves updates

**Alternative Flows:**
- A1: Invalid data entry
  1. System shows validation errors
  2. User corrects information

**Postconditions:**
- Patient data updated
- Audit log created

## 6. Sync Calendar (UC7)
**Actor:** Patient, Doctor
**Description:** Sync appointments with external calendar
**Preconditions:** User has external calendar configured

**Basic Flow:**
1. User requests calendar sync
2. System retrieves appointments
3. Generates calendar entries
4. Syncs with external calendar

**Alternative Flows:**
- A1: Sync failure
  1. System notifies user
  2. Provides manual export option

**Postconditions:**
- Calendar synchronized
- Sync status updated

## 7. Rate and Review (UC8)
**Actor:** Patient
**Description:** Submit feedback for completed appointments
**Preconditions:** 
- Appointment completed
- Patient logged in

**Basic Flow:**
1. Patient selects completed appointment
2. System displays review form
3. Patient submits rating/review
4. System validates submission
5. System publishes review

**Alternative Flows:**
- A1: Invalid submission
  1. System shows error message
  2. Patient corrects input

**Postconditions:**
- Review published
- Doctor rating updated

## 8. Monitor System (UC9)
**Actor:** IT Support
**Description:** Monitor system performance and security
**Preconditions:** IT Support has admin access

**Basic Flow:**
1. IT Support accesses monitoring dashboard
2. System displays metrics
3. IT Support reviews alerts
4. Takes necessary actions

**Alternative Flows:**
- A1: Critical system alert
  1. System sends immediate notification
  2. Triggers emergency response

**Postconditions:**
- System status updated
- Issues logged/resolved
