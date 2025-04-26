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
    Enum,
)
from ..settings.database import Base
from .utils import InstitutionTypeEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class HealthInstitution(Base):
    __tablename__ = "health_institutions"
    id = Column(Integer, primary_key=True)
    institution_name = Column(String(40), nullable=False)
    institution_email = Column(String(256), unique=True, index=True)
    institution_type = Column(Enum(InstitutionTypeEnum), nullable=False)
    institution_telephone = Column(String(15), nullable=False)
    institution_url = Column(String(100))
    health_professionals = relationship('InstitutionProfessional',back_populates='health_institution')



metadata = Base.metadata
