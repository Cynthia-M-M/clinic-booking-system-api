from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class PatientSchema(BaseModel):
    full_name: str
    email: str
    phone_number: str
    date_of_birth: Optional[date] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True 

class DoctorSchema(BaseModel):
    full_name: str
    specialization: str
    phone_number: str
    email: str
    years_of_experience: Optional[int] = 0

    class Config:
        orm_mode = True

class AppointmentSchema(BaseModel):
    appointment_datetime: datetime
    status: Optional[str] = 'Scheduled'
    notes: Optional[str] = None
    patient_id: int
    doctor_id: int

    class Config:
        orm_mode = True
