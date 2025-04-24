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
    Enum
)
from ..settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .enums import BloodGroupEnum
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True,index=True)
    blood_group = Column(Enum(BloodGroupEnum), nullable=False, index=True)
    is_blood_donor = Column(Boolean,nullable=False,index=True)
    user_id= Column(ForeignKey('users.id'))
    user= relationship ('User',back_populates='patient',uselist=False)

metadata= Base.metadata
