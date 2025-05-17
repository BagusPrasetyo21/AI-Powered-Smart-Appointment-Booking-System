# Patient Registration Workflow

```mermaid
flowchart TD
    Start([Start]) --> VisitRegistrationPage[Visit registration page]
    
    subgraph Patient [Patient]
        VisitRegistrationPage --> EnterBasicInfo[Enter basic personal information]
        EnterBasicInfo --> EnterContactInfo[Enter contact information]
        EnterContactInfo --> EnterMedicalHistory[Enter basic medical history]
        EnterMedicalHistory --> EnterInsuranceInfo[Enter insurance information]
        EnterInsuranceInfo --> AcceptTerms[Accept terms and privacy policy]
        AcceptTerms --> SubmitRegistration[Submit registration]
    end
    
    subgraph System [System]
        SubmitRegistration --> ValidateInputs{Validate all inputs}
        ValidateInputs -->|Invalid| HighlightErrors[Highlight validation errors]
        HighlightErrors --> EnterBasicInfo
        
        ValidateInputs -->|Valid| CheckExistingAccount{Check for existing account}
        CheckExistingAccount -->|Account exists| NotifyExistingAccount[Notify user of existing account]
        NotifyExistingAccount --> OfferPasswordReset[Offer password reset]
        OfferPasswordReset --> UserDecision{User decides}
        UserDecision -->|Reset password| TriggerReset[Trigger password reset flow]
        UserDecision -->|Create new| ConfirmNewAccount[Confirm new account creation]
        
        CheckExistingAccount -->|No account| CreateUserAccount[Create user account]
        ConfirmNewAccount --> CreateUserAccount
        
        CreateUserAccount --> GenerateVerificationToken[Generate verification token]
    end
    
    subgraph VerificationProcess [Verification Process]
        GenerateVerificationToken --> SendVerificationEmail[Send verification email]
        SendVerificationEmail --> WaitForVerification[Wait for email verification]
        
        WaitForVerification --> CheckVerification{User verifies email?}
        CheckVerification -->|Yes, within 24h| ActivateAccount[Activate account]
        CheckVerification -->|No, after 24h| ExpireToken[Expire verification token]
        ExpireToken --> UserReturns{User returns?}
        UserReturns -->|Yes| ResendVerification[Resend verification]
        UserReturns -->|No| ArchiveIncomplete[Archive incomplete registration]
        ResendVerification --> WaitForVerification
    end
    
    subgraph AccountSetup [Account Setup]
        ActivateAccount --> CreatePatientRecord[Create patient record in database]
        CreatePatientRecord --> AssignDefaultPermissions[Assign default permissions]
        AssignDefaultPermissions --> SendWelcomeEmail[Send welcome email]
        
        SendWelcomeEmail --> PromptCompleteProfile[Prompt to complete profile]
        PromptCompleteProfile --> OfferTutorial[Offer system tutorial]
    end
    
    OfferTutorial --> End([End])
    TriggerReset --> End
    ArchiveIncomplete --> End
```

## Activity Description

This activity diagram illustrates the complete workflow for patient registration in the AI-Powered Smart Appointment Booking System, from initial form completion through verification to account activation.

### Start/End Nodes
- **Start**: Patient initiates the registration process
- **End**: Patient account is created and activated, or process is abandoned

### Actions
1. **Visit registration page**: Patient accesses the registration form
2. **Enter basic personal information**: Patient provides name, date of birth, gender, etc.
3. **Enter contact information**: Patient provides phone, email, address
4. **Enter basic medical history**: Patient provides allergies, conditions, medications
5. **Enter insurance information**: Patient provides insurance details if applicable
6. **Accept terms and privacy policy**: Patient agrees to system terms
7. **Submit registration**: Patient submits the completed form
8. **Validate all inputs**: System checks for required fields and format validity
9. **Highlight validation errors**: System shows which fields need correction
10. **Check for existing account**: System verifies if email is already registered
11. **Create user account**: System generates new user credentials
12. **Generate verification token**: System creates a unique verification code
13. **Send verification email**: System sends email with verification link
14. **Activate account**: System enables full account functionality
15. **Create patient record**: System stores comprehensive patient information
16. **Send welcome email**: System sends onboarding information

### Decisions
1. **Validate all inputs**: Checks if all required information is provided correctly
2. **Check for existing account**: Determines if user already has an account
3. **User decides**: User chooses between password reset or new account
4. **User verifies email**: Checks if verification was completed
5. **User returns**: Determines if user returns after expired verification

### Parallel Actions
- The verification process runs independently of the main system flow:
  - Sending verification email
  - Monitoring for verification response
  - Handling verification expiration

### Swimlanes
- **Patient**: Actions performed by the patient during registration
- **System**: Core system actions for processing registration
- **Verification Process**: Actions related to email verification
- **Account Setup**: Actions related to finalizing the account
