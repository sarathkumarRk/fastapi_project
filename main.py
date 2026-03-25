from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

# Home
@app.get("/")
def home():
    return {"message": "Working"}

# Models
class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str

# Storage
doctors = []
patients = []

# Doctor APIs
@app.post("/doctors")
def create_doctor(doctor: Doctor):
    doctor_id = len(doctors) + 1
    new_doctor = {"id": doctor_id, **doctor.dict()}
    doctors.append(new_doctor)
    return {"message": "Doctor created", "data": new_doctor}

@app.get("/doctors")
def get_doctors():
    return doctors

@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

# Patient APIs
@app.post("/patients")
def create_patient(patient: Patient):
    patient_id = len(patients) + 1
    new_patient = {"id": patient_id, **patient.dict()}
    patients.append(new_patient)
    return {"message": "Patient created", "data": new_patient}

@app.get("/patients")
def get_patients():
    return patients