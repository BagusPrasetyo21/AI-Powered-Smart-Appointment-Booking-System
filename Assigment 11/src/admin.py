from datetime import datetime
from typing import List
from .enums import AdminRole

class Permission:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class SystemMetrics:
    def __init__(self, active_users: int, appointments_today: int, system_load: float):
        self.active_users = active_users
        self.appointments_today = appointments_today
        self.system_load = system_load

class Admin:
    def __init__(self, admin_id: str, name: str, email: str, role: AdminRole, 
                 permissions: List[Permission] = None, last_login: datetime = None):
        self._admin_id = admin_id
        self._name = name
        self._email = email
        self._role = role
        self._permissions = permissions if permissions else []
        self._last_login = last_login if last_login else datetime.now()
    
    @property
    def admin_id(self) -> str:
        return self._admin_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def role(self) -> AdminRole:
        return self._role
    
    @property
    def permissions(self) -> List[Permission]:
        return self._permissions
    
    @property
    def last_login(self) -> datetime:
        return self._last_login
    
    def generate_reports(self, report_type, date_range):
        """Generate reports based on type and date range"""
        from .report import Report, ReportType, DateRange
        import uuid
        
        report_id = str(uuid.uuid4())
        return Report(
            report_id=report_id,
            type=report_type,
            date_range=date_range,
            generated_by=self._admin_id
        )
    
    def manage_users(self, action: str, user_id: str) -> bool:
        """Manage users (create, update, delete, etc.)"""
        # Implementation would interact with user management service
        return True
    
    def configure_system(self, settings: dict) -> bool:
        """Configure system settings"""
        # Implementation would update system configuration
        return True
    
    def monitor_performance(self) -> SystemMetrics:
        """Monitor system performance"""
        # Implementation would retrieve actual metrics
        return SystemMetrics(
            active_users=100,
            appointments_today=50,
            system_load=0.75
        )
