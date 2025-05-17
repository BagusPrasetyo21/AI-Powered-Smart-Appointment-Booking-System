from datetime import datetime
import sys
import os
from typing import List, Optional

# Add the parent directory to the path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.medical_record import MedicalRecord, Diagnosis, Medication

class MedicalRecordBuilder:
    """
    Builder Pattern Implementation for MedicalRecord
    
    This builder allows step-by-step construction of a complex MedicalRecord
    object with many optional components.
    """
    
    def __init__(self, record_id: str, patient_id: str):
        self._record_id = record_id
        self._patient_id = patient_id
        self._diagnoses: List[Diagnosis] = []
        self._medications: List[Medication] = []
        self._allergies: List[str] = []
        self._notes: str = ""
        self._last_updated: datetime = datetime.now()
    
    def add_diagnosis(self, code: str, description: str, date: datetime) -> 'MedicalRecordBuilder':
        """Add a diagnosis to the medical record"""
        diagnosis = Diagnosis(code=code, description=description, date=date)
        self._diagnoses.append(diagnosis)
        self._last_updated = datetime.now()
        return self
    
    def add_medication(self, name: str, dosage: str, frequency: str, 
                      start_date: datetime, end_date: Optional[datetime] = None) -> 'MedicalRecordBuilder':
        """Add a medication to the medical record"""
        medication = Medication(
            name=name,
            dosage=dosage,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date
        )
        self._medications.append(medication)
        self._last_updated = datetime.now()
        return self
    
    def add_allergy(self, allergy: str) -> 'MedicalRecordBuilder':
        """Add an allergy to the medical record"""
        self._allergies.append(allergy)
        self._last_updated = datetime.now()
        return self
    
    def add_allergies(self, allergies: List[str]) -> 'MedicalRecordBuilder':
        """Add multiple allergies to the medical record"""
        self._allergies.extend(allergies)
        self._last_updated = datetime.now()
        return self
    
    def add_notes(self, notes: str) -> 'MedicalRecordBuilder':
        """Add notes to the medical record"""
        if self._notes:
            self._notes += f"\n{notes}"
        else:
            self._notes = notes
        self._last_updated = datetime.now()
        return self
    
    def build(self) -> MedicalRecord:
        """Build and return the final MedicalRecord object"""
        return MedicalRecord(
            record_id=self._record_id,
            patient_id=self._patient_id,
            diagnoses=self._diagnoses,
            medications=self._medications,
            allergies=self._allergies,
            notes=self._notes,
            last_updated=self._last_updated
        )

# Director class to demonstrate common building patterns
class MedicalRecordDirector:
    """
    Director class that knows how to use a builder to create common types of medical records
    """
    
    @staticmethod
    def create_empty_record(builder: MedicalRecordBuilder) -> MedicalRecord:
        """Create an empty medical record with just the IDs"""
        return builder.build()
    
    @staticmethod
    def create_basic_record(builder: MedicalRecordBuilder, allergies: List[str]) -> MedicalRecord:
        """Create a basic medical record with just allergies"""
        return builder.add_allergies(allergies).build()
    
    @staticmethod
    def create_comprehensive_record(
        builder: MedicalRecordBuilder,
        diagnoses: List[tuple],  # List of (code, description, date) tuples
        medications: List[tuple],  # List of (name, dosage, frequency, start_date, end_date) tuples
        allergies: List[str],
        notes: str
    ) -> MedicalRecord:
        """Create a comprehensive medical record with all components"""
        # Add diagnoses
        for code, description, date in diagnoses:
            builder.add_diagnosis(code, description, date)
        
        # Add medications
        for med_data in medications:
            if len(med_data) == 5:
                name, dosage, frequency, start_date, end_date = med_data
                builder.add_medication(name, dosage, frequency, start_date, end_date)
            else:
                name, dosage, frequency, start_date = med_data
                builder.add_medication(name, dosage, frequency, start_date)
        
        # Add allergies and notes
        builder.add_allergies(allergies).add_notes(notes)
        
        return builder.build()
