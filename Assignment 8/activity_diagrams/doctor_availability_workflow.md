# Doctor Availability Management Workflow

```mermaid
flowchart TD
    Start([Start]) --> DoctorLogin[Doctor logs in to system]
    
    subgraph Doctor [Doctor]
        DoctorLogin --> SelectCalendarView[Select calendar view]
        SelectCalendarView --> ViewCurrentSchedule[View current schedule]
        ViewCurrentSchedule --> ChooseAction{Choose action}
        
        ChooseAction -->|Set recurring availability| SetRecurringPattern[Set recurring availability pattern]
        ChooseAction -->|Block time slot| SelectTimeToBlock[Select time slot to block]
        ChooseAction -->|Unblock time slot| SelectTimeToUnblock[Select time slot to unblock]
        ChooseAction -->|Set vacation| SetVacationDates[Set vacation dates]
        
        SetRecurringPattern --> SpecifyWorkingDays[Specify working days]
        SpecifyWorkingDays --> SpecifyWorkingHours[Specify working hours]
        SpecifyWorkingHours --> SetBreakTimes[Set break times]
        SetBreakTimes --> SpecifyAppointmentDuration[Specify appointment duration]
        
        SelectTimeToBlock --> SpecifyBlockReason[Specify reason for blocking]
        SelectTimeToUnblock --> ConfirmUnblock[Confirm unblocking]
        SetVacationDates --> SpecifyVacationReason[Specify vacation reason]
    end
    
    subgraph System [System]
        SpecifyAppointmentDuration --> ValidatePattern{Validate pattern}
        ValidatePattern -->|Valid| SaveRecurringSchedule[Save recurring schedule]
        ValidatePattern -->|Invalid| DisplayPatternError[Display error message]
        DisplayPatternError --> SetRecurringPattern
        
        SpecifyBlockReason --> ValidateBlock{Validate block request}
        ValidateBlock -->|Valid| ProcessBlockRequest[Process block request]
        ValidateBlock -->|Has appointments| NotifyExistingAppointments[Notify about existing appointments]
        NotifyExistingAppointments --> ConfirmOverride{Confirm override?}
        ConfirmOverride -->|Yes| HandleExistingAppointments[Handle existing appointments]
        ConfirmOverride -->|No| CancelBlockRequest[Cancel block request]
        HandleExistingAppointments --> ProcessBlockRequest
        
        ConfirmUnblock --> ValidateUnblock{Validate unblock request}
        ValidateUnblock -->|Valid| ProcessUnblockRequest[Process unblock request]
        ValidateUnblock -->|Invalid| DisplayUnblockError[Display error message]
        DisplayUnblockError --> SelectTimeToUnblock
        
        SpecifyVacationReason --> ValidateVacation{Validate vacation request}
        ValidateVacation -->|Valid| ProcessVacationRequest[Process vacation request]
        ValidateVacation -->|Has appointments| NotifyVacationConflicts[Notify about appointment conflicts]
        NotifyVacationConflicts --> ConfirmVacationOverride{Confirm override?}
        ConfirmVacationOverride -->|Yes| HandleVacationAppointments[Handle affected appointments]
        ConfirmVacationOverride -->|No| CancelVacationRequest[Cancel vacation request]
        HandleVacationAppointments --> ProcessVacationRequest
    end
    
    subgraph Notification [Notification System]
        SaveRecurringSchedule --> UpdateAvailabilitySlots[Update availability slots]
        ProcessBlockRequest --> RemoveTimeSlot[Remove time slot from availability]
        ProcessUnblockRequest --> AddTimeSlot[Add time slot to availability]
        ProcessVacationRequest --> BlockVacationDates[Block all slots during vacation]
        
        UpdateAvailabilitySlots --> NotifyScheduleChange[Notify about schedule change]
        RemoveTimeSlot --> NotifySlotRemoved[Notify about removed slot]
        AddTimeSlot --> NotifySlotAdded[Notify about added slot]
        BlockVacationDates --> NotifyVacationSet[Notify about vacation dates]
    end
    
    NotifyScheduleChange --> End([End])
    NotifySlotRemoved --> End
    NotifySlotAdded --> End
    NotifyVacationSet --> End
    CancelBlockRequest --> End
    CancelVacationRequest --> End
```

## Activity Description

This activity diagram illustrates the workflow for doctors to manage their availability in the AI-Powered Smart Appointment Booking System, including setting regular hours, blocking time slots, and managing vacation time.

### Start/End Nodes
- **Start**: Doctor initiates the availability management process
- **End**: Availability settings are updated in the system

### Actions
1. **Doctor logs in to system**: Doctor authenticates with their credentials
2. **Select calendar view**: Doctor chooses daily, weekly, or monthly view
3. **View current schedule**: System displays current availability and appointments
4. **Set recurring availability pattern**: Doctor establishes regular working hours
5. **Specify working days**: Doctor selects which days of the week they work
6. **Specify working hours**: Doctor sets start and end times for each working day
7. **Set break times**: Doctor blocks out regular breaks (lunch, meetings, etc.)
8. **Specify appointment duration**: Doctor sets standard appointment length
9. **Select time slot to block**: Doctor chooses specific time to make unavailable
10. **Specify reason for blocking**: Doctor provides reason for unavailability
11. **Select time slot to unblock**: Doctor chooses previously blocked time to restore
12. **Set vacation dates**: Doctor selects dates for extended absence
13. **Update availability slots**: System generates individual appointment slots
14. **Remove time slot from availability**: System marks specific time as unavailable
15. **Add time slot to availability**: System makes previously blocked time available
16. **Block vacation dates**: System marks all affected dates as unavailable

### Decisions
1. **Choose action**: Doctor selects which availability management task to perform
2. **Validate pattern**: System checks if recurring schedule pattern is valid
3. **Validate block request**: System verifies if time slot can be blocked
4. **Confirm override**: Doctor decides whether to reschedule existing appointments
5. **Validate unblock request**: System checks if time slot can be unblocked
6. **Validate vacation request**: System verifies if vacation can be scheduled
7. **Confirm vacation override**: Doctor decides how to handle appointments during vacation

### Parallel Actions
- The notification system processes multiple updates simultaneously:
  - Updating availability slots
  - Notifying affected patients if appointments need rescheduling
  - Updating the booking system's available slots

### Swimlanes
- **Doctor**: Actions performed by the doctor
- **System**: Actions performed by the availability management system
- **Notification System**: Actions related to notifications and calendar updates
