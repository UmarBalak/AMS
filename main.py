from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import SessionLocal, Job, Candidate, Application, ApplicationStatusEnum
from pydantic import BaseModel
from typing import List
import datetime

# FastAPI app setup
app = FastAPI()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for input validation
class JobBase(BaseModel):
    title: str
    description: str
    company: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class CandidateBase(BaseModel):
    name: str
    email: str
    resume: str
    contact_number: str

class CandidateCreate(CandidateBase):
    pass

class CandidateResponse(CandidateBase):
    id: int

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    candidate_id: int
    job_id: int
    status: ApplicationStatusEnum = ApplicationStatusEnum.PENDING

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Job Application Management System"}

# CRUD for Jobs
@app.post("/jobs/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(
        title=job.title,
        description=job.description,
        company=job.company
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@app.get("/jobs/", response_model=List[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@app.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job: JobCreate, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db_job.title = job.title
    db_job.description = job.description
    db_job.company = job.company
    db.commit()
    db.refresh(db_job)
    return db_job

@app.delete("/jobs/{job_id}", status_code=204)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return {"msg": "Job deleted successfully"}

# CRUD for Candidates
@app.post("/candidates/", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    db_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        resume=candidate.resume,
        contact_number=candidate.contact_number
    )
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

@app.get("/candidates/", response_model=List[CandidateResponse])
def get_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()

@app.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    db_candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if db_candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return db_candidate

# CRUD for Applications
@app.post("/applications/", response_model=ApplicationResponse)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    db_application = Application(
        candidate_id=application.candidate_id,
        job_id=application.job_id,
        status=application.status
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@app.get("/applications/{candidate_id}", response_model=List[ApplicationResponse])
def get_applications(candidate_id: int, db: Session = Depends(get_db)):
    return db.query(Application).filter(Application.candidate_id == candidate_id).all()

@app.put("/applications/{application_id}", response_model=ApplicationResponse)
def update_application(application_id: int, application: ApplicationCreate, db: Session = Depends(get_db)):
    db_application = db.query(Application).filter(Application.id == application_id).first()
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db_application.status = application.status
    db.commit()
    db.refresh(db_application)
    return db_application

@app.delete("/applications/{application_id}", status_code=204)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    db_application = db.query(Application).filter(Application.id == application_id).first()
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(db_application)
    db.commit()
    return {"msg": "Application deleted successfully"}