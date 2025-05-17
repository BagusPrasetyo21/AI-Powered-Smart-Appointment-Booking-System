from datetime import datetime
from typing import List

class Diagnosis:
    def __init__(self, code: str, description: str, date: datetime):
        self.code = code
        self.description = description
        self.date = date

class Medication:
    def __init__(self, name: str, dosage: str, frequency: str, start_date: datetime, end_date: datetime = None):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date

class MedicalHistory:
    def __init__(self, patient_id: str, records: List['MedicalRecord']):
        self.patient_id = patient_id
        self.records = records

class MedicalRecord:
    def __init__(self, record_id: str, patient_id: str, diagnoses: List[Diagnosis] = None,
                 medications: List[Medication] = None, allergies: List[str] = None,
                 notes: str = "", last_updated: datetime = None):
        self._record_id = record_id
        self._patient_id = patient_id
        self._diagnoses = diagnoses if diagnoses else []
        self._medications = medications if medications else []
        self._allergies = allergies if allergies else []
        self._notes = notes
        self._last_updated = last_updated if last_updated else datetime.now()
    
    @property
    def record_id(self) -> str:
        return self._record_id
    
    @property
    def patient_id(self) -> str:
        return self._patient_id
    
    @property
    def diagnoses(self) -> List[Diagnosis]:
        return self._diagnoses
    
    @property
    def medications(self) -> List[Medication]:
        return self._medications
    
    @property
    def allergies(self) -> List[str]:
        return self._allergies
    
    @property
    def notes(self) -> str:
        return self._notes
    
    @property
    def last_updated(self) -> datetime:
        return self._last_updated
    
    def add_diagnosis(self, diagnosis: Diagnosis) -> bool:
        """Add a diagnosis to the medical record"""
        self._diagnoses.append(diagnosis)
        self._last_updated = datetime.now()
        return True
    
    def add_medication(self, medication: Medication) -> bool:
        """Add a medication to the medical record"""
        self._medications.append(medication)
        self._last_updated = datetime.now()
        return True
    
    def update_allergies(self, allergies: List[str]) -> bool:
        """Update the list of allergies"""
        self._allergies = allergies
        self._last_updated = datetime.now()
        return True
    
    def get_full_history(self) -> MedicalHistory:
        """Get the full medical history for this patient"""
        # In a real system, this would retrieve all records for the patient
        return MedicalHistory(patient_id=self._patient_id, records=[self])
