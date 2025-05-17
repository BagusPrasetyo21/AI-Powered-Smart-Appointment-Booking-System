from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum
from .time_slot import TimeSlot

class DayOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class TimeRange:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time

class Schedule:
    def __init__(self, schedule_id: str, doctor_id: str):
        self._schedule_id = schedule_id
        self._doctor_id = doctor_id
        self._working_hours: Dict[DayOfWeek, TimeRange] = {}
        self._blocked_slots: List[TimeSlot] = []
        self._available_slots: List[TimeSlot] = []
        self._last_updated = datetime.now()
    
    @property
    def schedule_id(self) -> str:
        return self._schedule_id
    
    @property
    def doctor_id(self) -> str:
        return self._doctor_id
    
    @property
    def working_hours(self) -> Dict[DayOfWeek, TimeRange]:
        return self._working_hours
    
    @property
    def blocked_slots(self) -> List[TimeSlot]:
        return self._blocked_slots
    
    @property
    def available_slots(self) -> List[TimeSlot]:
        return self._available_slots
    
    @property
    def last_updated(self) -> datetime:
        return self._last_updated
    
    def add_blocked_time(self, time_slot: TimeSlot) -> bool:
        """Add a blocked time slot"""
        self._blocked_slots.append(time_slot)
        # Remove from available slots if present
        self._available_slots = [slot for slot in self._available_slots 
                               if slot.slot_id != time_slot.slot_id]
        self._last_updated = datetime.now()
        return True
    
    def remove_blocked_time(self, time_slot: TimeSlot) -> bool:
        """Remove a blocked time slot"""
        self._blocked_slots = [slot for slot in self._blocked_slots 
                             if slot.slot_id != time_slot.slot_id]
        # Add to available slots
        self._available_slots.append(time_slot)
        self._last_updated = datetime.now()
        return True
    
    def get_available_slots(self, date: datetime) -> List[TimeSlot]:
        """Get available time slots for a specific date"""
        # Filter available slots for the given date
        day_slots = []
        for slot in self._available_slots:
            if (slot.start_time.year == date.year and 
                slot.start_time.month == date.month and 
                slot.start_time.day == date.day):
                day_slots.append(slot)
        return day_slots
    
    def check_availability(self, date_time: datetime) -> bool:
        """Check if a specific date and time is available"""
        # Check if the datetime falls within working hours for that day
        day_of_week = DayOfWeek(date_time.weekday())
        if day_of_week not in self._working_hours:
            return False
        
        working_range = self._working_hours[day_of_week]
        if not (working_range.start_time.time() <= date_time.time() <= working_range.end_time.time()):
            return False
        
        # Check if the datetime is not in any blocked slot
        for blocked in self._blocked_slots:
            if blocked.start_time <= date_time < blocked.end_time:
                return False
        
        return True
