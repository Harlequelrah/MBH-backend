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


class Compaign(Base):
    __tablename__ = 'compaigns'
    id = Column(Integer, primary_key=True)
    compaign_name = Column(String(30),nullable=False)
    compaign_type = Column(String(30),nullable=False)
    start_date = Column(DateTime,nullable=False)
    monthly_duration = Column(Integer)
    compaign_details = Column(Text,nullable=False)
    health_institution_id= Column(Integer,ForeignKey('health_institutions.id'),nullable=False)
    health_institution = relationship('HealthInstitution',back_populates='compaigns')
    patients = relationship('PatientCompaign',back_populates='compaign')


metadata= Base.metadata
