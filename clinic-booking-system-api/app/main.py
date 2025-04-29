from fastapi import FastAPI, HTTPException, Depends
from app.models.models import Patient, Doctor, Appointment
from app.schemas.schemas import PatientSchema, DoctorSchema, AppointmentSchema
from app.database.database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

# Create tables in the database (if not already created)
from app.models import models
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/patients/", response_model=PatientSchema)
def create_patient(patient: PatientSchema, db: Session = Depends(get_db)):
    db_patient = Patient(
        full_name=patient.full_name,
        email=patient.email,
        phone_number=patient.phone_number,
        date_of_birth=patient.date_of_birth,
        address=patient.address
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.get("/patients/", response_model=list[PatientSchema])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@app.get("/patients/{patient_id}", response_model=PatientSchema)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.put("/patients/{patient_id}", response_model=PatientSchema)
def update_patient(patient_id: int, patient: PatientSchema, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db_patient.full_name = patient.full_name
    db_patient.email = patient.email
    db_patient.phone_number = patient.phone_number
    db_patient.date_of_birth = patient.date_of_birth
    db_patient.address = patient.address
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.delete("/patients/{patient_id}", response_model=PatientSchema)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(db_patient)
    db.commit()
    return db_patient
