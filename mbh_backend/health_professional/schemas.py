from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from datetime import datetime
from ..settings.auth.schemas import UserBaseModel
from ..institution_professional.meta_models import MetaIPHealthInstitutionModel
from .meta_models import HealthProfessionalBaseModel

class HealthProfessionalCreateModel(HealthProfessionalBaseModel):
    user_id : int = Field(example=1)

class HealthProfessionalUpdateModel(HealthProfessionalCreateModel):
    pass


class HealthProfessionalPatchModel(BaseModel):
    biography: Optional[str ]= Field(
        example="I am a licensed physiotherapist with over 10 years of experience specializing in sports injuries and rehabilitation.",default=None
    )
    specialities : Optional[str ]= Field(example="physiotherapie",default=None)
    is_available : Optional[bool] = Field(example = True,default=None)
    user_id : Optional[int ]= Field(example=1,default=None)

class HealthProfessionalPydanticModel(HealthProfessionalBaseModel):
    id : int
    user : UserBaseModel
    health_institutions : List["MetaIPHealthInstitutionModel"]=[]
    class Config:
        from_attributes=True


