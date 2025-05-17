from datetime import datetime
from .enums import SlotStatus

class TimeSlot:
    def __init__(self, slot_id: str, start_time: datetime, end_time: datetime, 
                 status: SlotStatus = SlotStatus.AVAILABLE):
        self._slot_id = slot_id
        self._start_time = start_time
        self._end_time = end_time
        self._status = status
    
    @property
    def slot_id(self) -> str:
        return self._slot_id
    
    @property
    def start_time(self) -> datetime:
        return self._start_time
    
    @property
    def end_time(self) -> datetime:
        return self._end_time
    
    @property
    def status(self) -> SlotStatus:
        return self._status
    
    def is_available(self) -> bool:
        """Check if the time slot is available"""
        return self._status == SlotStatus.AVAILABLE
    
    def book(self) -> bool:
        """Book this time slot"""
        if self._status == SlotStatus.AVAILABLE:
            self._status = SlotStatus.BOOKED
            return True
        return False
    
    def release(self) -> bool:
        """Release this time slot (make it available again)"""
        if self._status == SlotStatus.BOOKED:
            self._status = SlotStatus.AVAILABLE
            return True
        return False
    
    def get_duration(self) -> int:
        """Get the duration of this time slot in minutes"""
        delta = self._end_time - self._start_time
        return int(delta.total_seconds() / 60)
