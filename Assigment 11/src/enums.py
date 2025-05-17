from enum import Enum, auto

class AppointmentStatus(Enum):
    SCHEDULED = auto()
    CONFIRMED = auto()
    CANCELLED = auto()
    COMPLETED = auto()
    NO_SHOW = auto()

class AppointmentType(Enum):
    REGULAR = auto()
    FOLLOW_UP = auto()
    EMERGENCY = auto()
    CONSULTATION = auto()
    PROCEDURE = auto()

class NotificationType(Enum):
    CONFIRMATION = auto()
    REMINDER = auto()
    CANCELLATION = auto()
    RESCHEDULING = auto()
    GENERAL = auto()

class NotificationStatus(Enum):
    PENDING = auto()
    SENT = auto()
    DELIVERED = auto()
    READ = auto()
    FAILED = auto()

class SlotStatus(Enum):
    AVAILABLE = auto()
    BOOKED = auto()
    BLOCKED = auto()

class AdminRole(Enum):
    SYSTEM_ADMIN = auto()
    USER_MANAGER = auto()
    REPORT_ANALYST = auto()
    SUPPORT_STAFF = auto()

class RecipientType(Enum):
    PATIENT = auto()
    DOCTOR = auto()
    ADMIN = auto()

class ReportType(Enum):
    APPOINTMENT_SUMMARY = auto()
    DOCTOR_PERFORMANCE = auto()
    PATIENT_STATISTICS = auto()
    SYSTEM_USAGE = auto()