# Test Cases for AI-Powered Smart Appointment Booking System

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------------|---------------|-------------|--------|-----------------|---------------|---------|
| TC001 | FR1 | User Registration | 1. Navigate to registration page<br>2. Enter valid details<br>3. Submit form<br>4. Verify email | - User account created<br>- Verification email received<br>- 2FA setup prompted | - | Pending |
| TC002 | FR2 | Appointment Booking | 1. Login as patient<br>2. Select "Book Appointment"<br>3. Choose doctor and time<br>4. Confirm booking | - Appointment created<br>- Confirmation email sent<br>- Doctor's schedule updated | - | Pending |
| TC003 | FR3 | Doctor Schedule Management | 1. Login as doctor<br>2. Access schedule manager<br>3. Add available slots<br>4. Save changes | - New slots visible in booking system<br>- No scheduling conflicts | - | Pending |
| TC004 | FR4 | Automated Reminders | 1. Create test appointment<br>2. Wait for 24-hour mark<br>3. Check notification delivery | - Reminder sent via email/SMS<br>- Correct appointment details included | - | Pending |
| TC005 | FR5 | Calendar Integration | 1. Enable calendar sync<br>2. Book appointment<br>3. Check external calendar | - Appointment synced<br>- Details correct in calendar | - | Pending |
| TC006 | FR6 | Patient Review System | 1. Complete appointment<br>2. Access review section<br>3. Submit rating/review | - Review submitted<br>- Doctor rating updated | - | Pending |
| TC007 | FR7 | Admin Report Generation | 1. Login as admin<br>2. Access reports section<br>3. Generate monthly report | - Report generated<br>- All metrics included | - | Pending |
| TC008 | FR8 | Support Ticket Management | 1. Create support ticket<br>2. Assign to IT support<br>3. Process and resolve | - Ticket tracked<br>- Resolution documented | - | Pending |

## Non-Functional Test Cases

### Performance Tests

| Test Case ID | Requirement | Description | Steps | Expected Result | Actual Result | Status |
|--------------|------------|-------------|--------|-----------------|---------------|---------|
| NFT001 | NFR-Scalability | Concurrent User Load Test | 1. Simulate 1000 concurrent users<br>2. Monitor system performance<br>3. Check response times | - System remains responsive<br>- Response time ≤ 2 seconds<br>- No errors | - | Pending |
| NFT002 | NFR-Security | Security Penetration Test | 1. Attempt SQL injection<br>2. Test XSS vulnerabilities<br>3. Check password policies | - All attacks blocked<br>- Security logs generated<br>- Alerts triggered | - | Pending |

### Test Scenarios for Non-Functional Requirements

#### Performance Test Scenario
**Objective:** Verify system performance under peak load
- **Setup:**
  - Generate 1000 virtual users
  - Each user performs common actions (booking, searching)
  - Monitor for 1 hour during peak time
- **Success Criteria:**
  - Average response time < 2 seconds
  - Zero system crashes
  - CPU usage < 80%
  - Memory usage < 90%

#### Security Test Scenario
**Objective:** Validate data encryption and access controls
- **Setup:**
  - Attempt unauthorized access to patient records
  - Test data encryption during transmission
  - Verify audit logging
- **Success Criteria:**
  - All sensitive data encrypted
  - Failed access attempts logged
  - RBAC properly enforced
  - Audit trail complete
