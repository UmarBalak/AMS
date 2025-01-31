import os
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer, ForeignKey, Enum, Float
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import enum
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is missing")

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums for Job Status and Roles
class ApplicationStatusEnum(str, enum.Enum):
    PENDING = "Pending"
    REVIEWED = "Reviewed"
    INTERVIEWED = "Interviewed"
    HIRED = "Hired"
    REJECTED = "Rejected"

class RoleEnum(str, enum.Enum):
    ADMIN = "Admin"
    RECRUITER = "Recruiter"
    CANDIDATE = "Candidate"

# Job Model
class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    company = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    applications = relationship("Application", back_populates="job")

# Candidate Model
class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    resume = Column(String, nullable=True)
    contact_number = Column(String, nullable=True)
    applications = relationship("Application", back_populates="candidate")

# Application Model
class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(Enum(ApplicationStatusEnum), default=ApplicationStatusEnum.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    candidate = relationship("Candidate", back_populates="applications")
    job = relationship("Job", back_populates="applications")

# Create tables
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Error while creating tables: {e}")
