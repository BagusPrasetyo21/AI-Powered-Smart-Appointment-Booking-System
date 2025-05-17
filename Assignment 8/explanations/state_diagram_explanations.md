# State Diagram Explanations

This document provides detailed explanations for each state transition diagram, highlighting how they map to the functional requirements of the AI-Powered Smart Appointment Booking System.

## 1. Appointment State Diagram

The Appointment state diagram models the lifecycle of an appointment from initial request through completion and review.

### Key States and Transitions

- **Requested → Scheduled**: This transition represents the confirmation of an appointment request, which directly addresses FR-001 (Allow patients to book appointments online).
- **Scheduled → Rescheduled**: This transition supports FR-003 (Allow patients to reschedule appointments) by modeling how appointments change when rescheduled.
- **Scheduled → Canceled**: This transition implements FR-004 (Allow patients to cancel appointments) by showing the cancellation flow.
- **Completed → Reviewed**: This transition supports FR-012 (Allow patients to rate and review appointments) by connecting the appointment completion to the review process.

### Mapping to Functional Requirements

- The "CheckedIn" state addresses FR-008 (Track patient arrival status) by representing the moment when a patient arrives for their appointment.
- The "InProgress" and "Completed" states support FR-009 (Allow doctors to update appointment status) by modeling the progression of an active appointment.
- The guard condition "Patient must have valid account" on the Requested state implements FR-002 (Require patient registration before booking).
- The guard condition "Selected time must be available" on the Scheduled state supports FR-005 (Prevent double-booking of appointments).

## 2. User Account State Diagram

The User Account state diagram models the lifecycle of user accounts in the system, from registration through various active and inactive states.

### Key States and Transitions

- **Registered → PendingVerification → Active**: This sequence implements FR-002 (Require patient registration before booking) by ensuring proper account verification.
- **Active → Locked**: This transition supports FR-023 (Implement account security measures) by modeling how accounts are protected from unauthorized access.
- **Active → Suspended**: This transition implements FR-024 (Allow administrators to manage user accounts) by showing administrative control over accounts.
- **Deactivated → Deleted**: This transition supports FR-025 (Comply with data retention policies) by modeling the account deletion process.

### Mapping to Functional Requirements

- The "PendingVerification" state addresses FR-026 (Verify user email addresses) by requiring email verification before activation.
- The "Inactive" state supports FR-027 (Automatically flag inactive accounts) by representing accounts without recent activity.
- The guard condition "Valid email and required fields" on the Registered state implements FR-002 (Require complete registration information).
- The transition from "Deactivated" to "Active" within 30 days supports FR-028 (Allow account reactivation within grace period).

## 3. Doctor Availability State Diagram

The Doctor Availability state diagram models how time slots transition between different states of availability in the system.

### Key States and Transitions

- **Created → Available**: This transition implements FR-006 (Allow doctors to set availability) by making time slots visible for booking.
- **Available → Reserved → Confirmed**: This sequence supports FR-001 (Allow patients to book appointments online) by modeling the booking process.
- **Available → Blocked**: This transition implements FR-007 (Allow doctors to block time slots) by showing how doctors can make specific times unavailable.
- **Confirmed → NoShow**: This transition supports FR-010 (Track no-show appointments) by modeling appointment non-attendance.

### Mapping to Functional Requirements

- The "Reserved" state addresses FR-005 (Prevent double-booking) by temporarily holding a slot during the booking process.
- The "Canceled → Available" transition supports FR-011 (Automatically free canceled slots) by returning canceled appointments to the available pool.
- The guard condition "Must be future date/time" on the Created state implements FR-029 (Prevent creation of past availability).
- The "Expired" state supports FR-030 (Automatically manage passed time slots) by handling slots that were never booked.

## 4. Patient Record State Diagram

The Patient Record state diagram models the lifecycle of patient medical records in the system.

### Key States and Transitions

- **Created → Incomplete → Complete**: This sequence implements FR-013 (Collect comprehensive patient information) by ensuring all required data is gathered.
- **Complete → Active**: This transition supports FR-014 (Validate patient information) by representing the verification process.
- **Active → Updated**: This transition implements FR-015 (Allow updating of patient records) by modeling the record update process.
- **Active → Archived**: This transition supports FR-025 (Comply with data retention policies) by modeling the archiving of inactive records.

### Mapping to Functional Requirements

- The "Locked" state addresses FR-016 (Protect sensitive patient information) by restricting access during security concerns.
- The "Flagged" state supports FR-017 (Identify inconsistent patient data) by marking records that need attention.
- The guard condition "All mandatory fields filled and validated" on the Complete state implements FR-013 (Ensure complete patient records).
- The transition from "Archived" to "Active" supports FR-018 (Reactivate archived patient records) when patients return.

## 5. Notification State Diagram

The Notification state diagram models how system notifications progress from creation through delivery and response.

### Key States and Transitions

- **Created → Queued → Sent**: This sequence implements FR-019 (Generate automated notifications) by showing the notification creation process.
- **Sent → Delivered → Read**: This sequence supports FR-020 (Track notification delivery status) by modeling successful notification delivery.
- **Sent → Failed → Retrying**: This transition implements FR-021 (Handle failed notification delivery) by showing retry attempts.
- **Delivered → Acknowledged**: This transition supports FR-022 (Track user response to notifications) by modeling user interaction with notifications.

### Mapping to Functional Requirements

- The "PermanentlyFailed" state addresses FR-021 (Handle failed notification delivery) by representing notifications that cannot be delivered.
- The "Expired" state supports FR-031 (Manage notification expiration) by handling notifications that are no longer relevant.
- The guard condition "Valid recipient contact info" on the Queued state implements FR-032 (Validate contact information before sending).
- The guard condition "Retry count < 3" on the Retrying state supports FR-021 (Limit retry attempts for failed notifications).

## 6. Review State Diagram

The Review state diagram models how patient reviews progress from initial prompt through submission, moderation, and publication.

### Key States and Transitions

- **Prompted → Draft → Submitted**: This sequence implements FR-012 (Allow patients to rate and review appointments) by modeling the review creation process.
- **Submitted → UnderModeration → Published**: This sequence supports FR-033 (Moderate user-generated content) by ensuring reviews are appropriate.
- **Published → Responded**: This transition implements FR-034 (Allow doctors to respond to reviews) by connecting reviews to provider responses.
- **Published → Edited**: This transition supports FR-035 (Allow patients to edit reviews) by modeling the review update process.

### Mapping to Functional Requirements

- The "Rejected" state addresses FR-033 (Moderate user-generated content) by handling inappropriate reviews.
- The "Abandoned" state supports FR-036 (Track incomplete review submissions) by representing unfinished reviews.
- The guard condition "Patient must have attended appointment" on the Draft state implements FR-037 (Verify appointment completion before review).
- The note "Sent 24 hours after appointment completion" supports FR-038 (Time review requests appropriately).

## 7. System Access State Diagram

The System Access state diagram models how users authenticate, gain authorization, and maintain active sessions in the system.

### Key States and Transitions

- **Unauthenticated → AuthenticationAttempt → Authenticated**: This sequence implements FR-039 (Secure user authentication) by modeling the login process.
- **Authenticated → Authorized**: This transition supports FR-040 (Implement role-based access control) by verifying user permissions.
- **Active → Idle → SessionTimeout**: This sequence implements FR-041 (Manage user session timeouts) by modeling session inactivity handling.
- **FailedAttempt → Locked**: This transition supports FR-042 (Prevent brute force attacks) by locking accounts after multiple failures.

### Mapping to Functional Requirements

- The "PartialAccess" state addresses FR-043 (Provide granular permission management) by representing limited system access.
- The "PermissionRequest" state supports FR-044 (Allow users to request additional permissions) by modeling the permission escalation process.
- The guard condition "Attempts < 5" on the FailedAttempt state implements FR-042 (Limit failed login attempts).
- The note "Triggered after 10 minutes of inactivity" on the Idle state supports FR-041 (Set appropriate inactivity thresholds).
