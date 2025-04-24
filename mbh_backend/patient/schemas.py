from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from datetime import datetime
from .enums import BloodGroupEnum
from ..settings.auth.schemas import UserBaseModel

class PatientBaseModel(BaseModel):
    blood_group :BloodGroupEnum = Field(example=BloodGroupEnum.A_POSITIVE)
    is_blood_donor : bool = Field(example=True)

class PatientCreateModel(PatientBaseModel):
    user_id : int = Field(example=1)


class PatientUpdateModel(PatientCreateModel):
    pass
class PatientPatchModel(BaseModel):
    blood_group : Optional[BloodGroupEnum] = Field(example=BloodGroupEnum.A_POSITIVE,default=None)
    is_blood_donor : Optional[bool] = Field(example=True,default=None)
    user_id : Optional[int] = Field(example=1,default=None)

class PatientPydanticModel(PatientBaseModel):
    id:int
    user : UserBaseModel
    class Config:
        from_attributes=True


