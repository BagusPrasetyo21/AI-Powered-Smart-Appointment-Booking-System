from datetime import datetime

class Rating:
    def __init__(self, rating_id: str, patient_id: str, appointment_id: str, doctor_id: str,
                 score: int, comment: str, timestamp: datetime = None, is_edited: bool = False):
        self._rating_id = rating_id
        self._patient_id = patient_id
        self._appointment_id = appointment_id
        self._doctor_id = doctor_id
        self._score = score
        self._comment = comment
        self._timestamp = timestamp if timestamp else datetime.now()
        self._is_edited = is_edited
    
    @property
    def rating_id(self) -> str:
        return self._rating_id
    
    @property
    def patient_id(self) -> str:
        return self._patient_id
    
    @property
    def appointment_id(self) -> str:
        return self._appointment_id
    
    @property
    def doctor_id(self) -> str:
        return self._doctor_id
    
    @property
    def score(self) -> int:
        return self._score
    
    @property
    def comment(self) -> str:
        return self._comment
    
    @property
    def timestamp(self) -> datetime:
        return self._timestamp
    
    @property
    def is_edited(self) -> bool:
        return self._is_edited
    
    def submit(self) -> bool:
        """Submit the rating"""
        # In a real system, this would save to a database
        return True
    
    def edit(self, new_score: int, new_comment: str) -> bool:
        """Edit the rating with new score and comment"""
        self._score = new_score
        self._comment = new_comment
        self._is_edited = True
        self._timestamp = datetime.now()  # Update timestamp to reflect edit time
        return True
    
    def delete(self) -> bool:
        """Delete the rating"""
        # In a real system, this would remove from database or mark as deleted
        return True
