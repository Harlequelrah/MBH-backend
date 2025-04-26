from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from ..settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class PatientCompaign(Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer,ForeignKey('patients.id'),nullable=False)
    patient = relationship('Patient',back_populates='compaigns')
    compaign_id = Column(Integer,ForeignKey('compaigns.id'),nullable=False)
    compaign = relationship('Compaign',back_populates='patients')

metadata= Base.metadata
