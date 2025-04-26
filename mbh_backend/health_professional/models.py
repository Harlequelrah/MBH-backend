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


class HealthProfessional(Base):
    __tablename__ = 'health_professionals'
    id = Column(Integer, primary_key=True,index=True)
    biography=Column(Text)
    specialities = Column(String(100),nullable=False)
    is_available = Column(Boolean , nullable=False,index=True)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    user = relationship('User',back_populates='health_professional',uselist=False)
    health_institutions= relationship('InstitutionProfessional',back_populates='health_professional')

metadata= Base.metadata
