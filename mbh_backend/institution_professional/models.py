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


class InstitutionProfessional(Base):
    __tablename__ = 'institution_professionals'
    id = Column(Integer, primary_key=True)
    health_institution_id = Column(Integer,ForeignKey('health_institutions.id'),nullable=False)
    health_professional_id = Column(Integer,ForeignKey('health_professionals.id'),nullable=False)
    health_institution= relationship('HealthInstitution',back_populates='health_institutions')
    health_professional= relationship('HealthProfessional',back_populates='health_professionals')

metadata= Base.metadata
