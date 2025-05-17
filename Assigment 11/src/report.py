from datetime import datetime
from enum import Enum, auto
from typing import Any

class ReportType(Enum):
    APPOINTMENT_SUMMARY = auto()
    DOCTOR_PERFORMANCE = auto()
    PATIENT_STATISTICS = auto()
    SYSTEM_USAGE = auto()

class DateRange:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

class Chart:
    def __init__(self, title: str, data: Any, chart_type: str):
        self.title = title
        self.data = data
        self.chart_type = chart_type

class File:
    def __init__(self, name: str, content: bytes, format: str):
        self.name = name
        self.content = content
        self.format = format

class Report:
    def __init__(self, report_id: str, type: ReportType, date_range: DateRange,
                 generated_by: str, data: Any = None):
        self._report_id = report_id
        self._type = type
        self._date_range = date_range
        self._generated_by = generated_by
        self._created_at = datetime.now()
        self._data = data if data else {}
    
    @property
    def report_id(self) -> str:
        return self._report_id
    
    @property
    def type(self) -> ReportType:
        return self._type
    
    @property
    def date_range(self) -> DateRange:
        return self._date_range
    
    @property
    def generated_by(self) -> str:
        return self._generated_by
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @property
    def data(self) -> Any:
        return self._data
    
    def export(self, format: str) -> File:
        """Export the report in the specified format"""
        # Implementation would convert report data to the specified format
        content = bytes(f"Report {self._report_id} in {format} format", 'utf-8')
        return File(
            name=f"report_{self._report_id}.{format.lower()}",
            content=content,
            format=format
        )
    
    def visualize(self) -> Chart:
        """Visualize the report data as a chart"""
        # Implementation would generate a chart from the report data
        return Chart(
            title=f"Report {self._type.name}",
            data=self._data,
            chart_type="bar"  # Default chart type
        )
    
    def share(self, recipients: list) -> bool:
        """Share the report with the specified recipients"""
        # Implementation would send the report to recipients
        return True
