# Appointment Reminder Workflow

```mermaid
flowchart TD
    Start([Start]) --> ScheduledTask[Scheduled reminder task runs]
    
    subgraph System [System]
        ScheduledTask --> QueryAppointments[Query upcoming appointments]
        QueryAppointments --> FilterAppointments[Filter appointments by time window]
        FilterAppointments --> CheckReminderStatus{Check if reminder already sent}
        
        CheckReminderStatus -->|Not sent| ProcessEligible[Process eligible appointments]
        CheckReminderStatus -->|Already sent| SkipAppointment[Skip appointment]
        
        ProcessEligible --> CheckPatientPreferences{Check patient notification preferences}
    end
    
    subgraph NotificationPreparation [Notification Preparation]
        CheckPatientPreferences --> PrepareEmailReminder[Prepare email reminder]
        CheckPatientPreferences --> PrepareSMSReminder[Prepare SMS reminder]
        CheckPatientPreferences --> PrepareAppNotification[Prepare app notification]
        
        PrepareEmailReminder --> IncludeAppointmentDetails1[Include appointment details]
        PrepareSMSReminder --> IncludeAppointmentDetails2[Include appointment details]
        PrepareAppNotification --> IncludeAppointmentDetails3[Include appointment details]
        
        IncludeAppointmentDetails1 --> AddConfirmationLink1[Add confirmation link]
        IncludeAppointmentDetails2 --> AddConfirmationLink2[Add confirmation link]
        IncludeAppointmentDetails3 --> AddConfirmationLink3[Add confirmation link]
        
        AddConfirmationLink1 --> AddRescheduleLink1[Add reschedule link]
        AddConfirmationLink2 --> AddRescheduleLink2[Add reschedule link]
        AddConfirmationLink3 --> AddRescheduleLink3[Add reschedule link]
        
        AddRescheduleLink1 --> AddCancellationLink1[Add cancellation link]
        AddRescheduleLink2 --> AddCancellationLink2[Add cancellation link]
        AddRescheduleLink3 --> AddCancellationLink3[Add cancellation link]
    end
    
    subgraph DeliverySystem [Delivery System]
        AddCancellationLink1 --> SendEmail[Send email reminder]
        AddCancellationLink2 --> SendSMS[Send SMS reminder]
        AddCancellationLink3 --> SendAppNotification[Send app notification]
        
        SendEmail --> LogEmailAttempt[Log email delivery attempt]
        SendSMS --> LogSMSAttempt[Log SMS delivery attempt]
        SendAppNotification --> LogAppAttempt[Log app notification attempt]
        
        LogEmailAttempt --> CheckEmailDelivery{Email delivered?}
        LogSMSAttempt --> CheckSMSDelivery{SMS delivered?}
        LogAppAttempt --> CheckAppDelivery{App notification delivered?}
        
        CheckEmailDelivery -->|Yes| MarkEmailSent[Mark email reminder as sent]
        CheckEmailDelivery -->|No| QueueEmailRetry[Queue for retry]
        
        CheckSMSDelivery -->|Yes| MarkSMSSent[Mark SMS reminder as sent]
        CheckSMSDelivery -->|No| QueueSMSRetry[Queue for retry]
        
        CheckAppDelivery -->|Yes| MarkAppSent[Mark app reminder as sent]
        CheckAppDelivery -->|No| QueueAppRetry[Queue for retry]
    end
    
    subgraph ResponseTracking [Response Tracking]
        MarkEmailSent --> TrackReminderStatus[Track reminder status]
        MarkSMSSent --> TrackReminderStatus
        MarkAppSent --> TrackReminderStatus
        
        TrackReminderStatus --> WaitForResponse[Wait for patient response]
        WaitForResponse --> MonitorResponse{Monitor response}
        
        MonitorResponse -->|Confirmed| UpdateAppointmentStatus1[Update appointment as confirmed]
        MonitorResponse -->|Reschedule requested| TriggerRescheduleFlow[Trigger reschedule workflow]
        MonitorResponse -->|Cancellation requested| TriggerCancellationFlow[Trigger cancellation workflow]
        MonitorResponse -->|No response| CheckFollowUpNeeded{Check if follow-up needed}
        
        CheckFollowUpNeeded -->|Yes| ScheduleFollowUp[Schedule follow-up reminder]
        CheckFollowUpNeeded -->|No| MarkReminderComplete[Mark reminder process complete]
    end
    
    SkipAppointment --> End([End])
    QueueEmailRetry --> End
    QueueSMSRetry --> End
    QueueAppRetry --> End
    UpdateAppointmentStatus1 --> End
    TriggerRescheduleFlow --> End
    TriggerCancellationFlow --> End
    ScheduleFollowUp --> End
    MarkReminderComplete --> End
```

## Activity Description

This activity diagram illustrates the automated workflow for sending appointment reminders to patients in the AI-Powered Smart Appointment Booking System, including delivery through multiple channels and tracking patient responses.

### Start/End Nodes
- **Start**: Scheduled reminder task initiates
- **End**: Reminder process completes with appropriate status updates

### Actions
1. **Scheduled reminder task runs**: System automatically triggers the reminder process at predetermined intervals
2. **Query upcoming appointments**: System retrieves all appointments from the database
3. **Filter appointments by time window**: System identifies appointments within the reminder timeframe (e.g., 24 hours before appointment)
4. **Process eligible appointments**: System prepares to send reminders for appointments that haven't received them yet
5. **Prepare email/SMS/app notification**: System generates reminder content for different channels
6. **Include appointment details**: System adds date, time, doctor name, and location to the reminder
7. **Add confirmation/reschedule/cancellation links**: System includes action links for patient response
8. **Send reminders**: System delivers notifications through selected channels
9. **Log delivery attempts**: System records whether notifications were successfully delivered
10. **Mark reminders as sent**: System updates the database to prevent duplicate reminders
11. **Track reminder status**: System monitors which reminders have been sent through which channels
12. **Wait for patient response**: System awaits patient interaction with the reminder
13. **Update appointment status**: System records patient confirmation
14. **Schedule follow-up reminder**: System sets up additional reminder if no response is received

### Decisions
1. **Check if reminder already sent**: Prevents duplicate reminders
2. **Check patient notification preferences**: Determines which channels to use for each patient
3. **Email/SMS/App notification delivered?**: Verifies successful delivery
4. **Monitor response**: Tracks different possible patient actions
5. **Check if follow-up needed**: Determines if additional reminder is required

### Parallel Actions
- The notification preparation system handles multiple formats simultaneously:
  - Email reminder preparation
  - SMS reminder preparation
  - App notification preparation
- The delivery system sends reminders through multiple channels in parallel

### Swimlanes
- **System**: Core system actions for identifying appointments needing reminders
- **Notification Preparation**: Actions related to creating reminder content
- **Delivery System**: Actions related to sending reminders through different channels
- **Response Tracking**: Actions related to monitoring and processing patient responses
