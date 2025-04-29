from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database.database import Base

class Patient(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    date_of_birth = Column(Date)
    address = Column(Text)
    
class Doctor(Base):
    __tablename__ = 'doctors'
    doctor_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    years_of_experience = Column(Integer, default=0)

class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'))
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'))
    appointment_datetime = Column(DateTime, nullable=False)
    status = Column(Enum('Scheduled', 'Completed', 'Cancelled', name='status'), default='Scheduled')
    notes = Column(Text)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

Patient.appointments = relationship("Appointment", back_populates="patient")
Doctor.appointments = relationship("Appointment", back_populates="doctor")
