import threading
from typing import Dict, Any, Optional

class SystemConfiguration:
    """
    Singleton Pattern Implementation
    
    This class ensures that only one instance of the system configuration exists
    throughout the application, providing a global point of access.
    """
    
    # Class variable to hold the single instance
    _instance: Optional['SystemConfiguration'] = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Ensure only one instance is created (double-checked locking pattern)"""
        if cls._instance is None:
            with cls._lock:
                # Check again after acquiring the lock
                if cls._instance is None:
                    cls._instance = super(SystemConfiguration, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize the configuration (only once)"""
        if not getattr(self, '_initialized', False):
            self._config: Dict[str, Any] = {
                'app_name': 'AI-Powered Smart Appointment Booking System',
                'version': '1.0.0',
                'database_url': 'jdbc:mysql://localhost:3306/appointment_db',
                'max_appointments_per_day': 20,
                'notification_enabled': True,
                'reminder_hours_before': 24,
                'working_hours': {
                    'start': '09:00',
                    'end': '17:00'
                },
                'appointment_duration_minutes': 30,
                'time_zone': 'UTC'
            }
            self._initialized = True
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key"""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value"""
        self._config[key] = value
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration values"""
        return self._config.copy()  # Return a copy to prevent direct modification
    
    def reset(self) -> None:
        """Reset configuration to default values (for testing)"""
        self._initialized = False
        self.__init__()

class DatabaseConnection:
    """
    Another Singleton example: Database Connection
    
    This class ensures that only one database connection exists
    throughout the application, which is a common use case for Singleton.
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, connection_string: str = None):
        if not getattr(self, '_initialized', False):
            # Get connection string from SystemConfiguration if not provided
            if connection_string is None:
                config = SystemConfiguration()
                connection_string = config.get('database_url')
            
            self._connection_string = connection_string
            self._connected = False
            self._initialized = True
            print(f"Initializing database connection to: {connection_string}")
    
    def connect(self) -> bool:
        """Establish the database connection"""
        if not self._connected:
            # In a real system, this would actually connect to the database
            print(f"Connecting to database: {self._connection_string}")
            self._connected = True
        return self._connected
    
    def disconnect(self) -> bool:
        """Close the database connection"""
        if self._connected:
            # In a real system, this would actually close the connection
            print("Disconnecting from database")
            self._connected = False
        return not self._connected
    
    def execute_query(self, query: str) -> list:
        """Execute a query on the database"""
        if not self._connected:
            self.connect()
        
        # In a real system, this would execute the query and return results
        print(f"Executing query: {query}")
        return []  # Placeholder
