from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from datetime import datetime
from ..health_professional.meta_models import MetaHealthProfessionalModel
from ..health_institution.meta_models import MetaHealthInstitutionModel


class InstitutionProfessionalBaseModel(BaseModel):
    health_institution_id : int = Field(example=1)
    health_professioanl_id : int = Field(example=2)

class InstitutionProfessionalCreateModel(InstitutionProfessionalBaseModel):
    pass

class InstitutionProfessionalUpdateModel(InstitutionProfessionalBaseModel):
    pass

class InstitutionProfessionalPatchModel(BaseModel):
    health_institution_id : Optional[int] = Field(example=1,default=None)
    health_professioanl_id : Optional[int] = Field(example=2,default=None)

class InstitutionProfessionalPydanticModel(BaseModel):
    id:int
    health_professional : MetaHealthProfessionalModel
    health_institution : MetaHealthInstitutionModel
    class Config:
        from_attributes=True


