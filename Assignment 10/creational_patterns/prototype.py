import copy
import uuid
import sys
import os
from datetime import datetime, timedelta
from typing import Dict, List

# Add the parent directory to the path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.time_slot import TimeSlot
from src.enums import SlotStatus

class TimeSlotPrototype:
    """
    Prototype Pattern Implementation for TimeSlot
    
    This class allows cloning of TimeSlot objects to efficiently create
    multiple similar time slots without the cost of initialization.
    """
    
    def __init__(self, start_time: datetime, end_time: datetime, status: SlotStatus = SlotStatus.AVAILABLE):
        self._slot_id = str(uuid.uuid4())
        self._start_time = start_time
        self._end_time = end_time
        self._status = status
    
    def clone(self) -> TimeSlot:
        """Create a deep copy of the time slot with a new ID"""
        # Create a new TimeSlot with the same properties but a new ID
        return TimeSlot(
            slot_id=str(uuid.uuid4()),
            start_time=copy.deepcopy(self._start_time),
            end_time=copy.deepcopy(self._end_time),
            status=self._status
        )
    
    def clone_with_new_time(self, start_time: datetime, end_time: datetime) -> TimeSlot:
        """Clone the time slot but with new start and end times"""
        return TimeSlot(
            slot_id=str(uuid.uuid4()),
            start_time=start_time,
            end_time=end_time,
            status=self._status
        )
    
    def clone_with_offset(self, days: int = 0, hours: int = 0, minutes: int = 0) -> TimeSlot:
        """Clone the time slot but offset by the specified time"""
        offset = timedelta(days=days, hours=hours, minutes=minutes)
        new_start = self._start_time + offset
        new_end = self._end_time + offset
        
        return TimeSlot(
            slot_id=str(uuid.uuid4()),
            start_time=new_start,
            end_time=new_end,
            status=self._status
        )

class TimeSlotCache:
    """
    Registry for TimeSlot prototypes
    
    This class stores and manages TimeSlot prototypes for efficient creation
    of new time slots based on predefined templates.
    """
    
    def __init__(self):
        self._prototypes: Dict[str, TimeSlotPrototype] = {}
    
    def add_prototype(self, name: str, prototype: TimeSlotPrototype) -> None:
        """Add a prototype to the registry"""
        self._prototypes[name] = prototype
    
    def get_prototype(self, name: str) -> TimeSlotPrototype:
        """Get a prototype from the registry"""
        return self._prototypes.get(name)
    
    def create_time_slot(self, name: str) -> TimeSlot:
        """Create a new time slot from a named prototype"""
        prototype = self.get_prototype(name)
        if prototype:
            return prototype.clone()
        return None
    
    def create_daily_slots(self, name: str, days: int) -> List[TimeSlot]:
        """Create time slots for multiple consecutive days based on a prototype"""
        prototype = self.get_prototype(name)
        if not prototype:
            return []
        
        slots = []
        for day in range(days):
            slots.append(prototype.clone_with_offset(days=day))
        
        return slots
    
    def create_weekly_recurring_slot(self, name: str, weeks: int) -> List[TimeSlot]:
        """Create time slots for the same day of the week for multiple weeks"""
        prototype = self.get_prototype(name)
        if not prototype:
            return []
        
        slots = []
        for week in range(weeks):
            slots.append(prototype.clone_with_offset(days=week * 7))
        
        return slots
