from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from datetime import datetime

from .meta_models import PatientCompaignBaseModel

class PatientCompaignCreateModel(PatientCompaignBaseModel):
    pass

class PatientCompaignUpdateModel(PatientCompaignBaseModel):
    pass

class PatientCompaignPatchModel(BaseModel):
    patient_id:Optional[int]=Field(example=1,default=None)
    compain_id:Optional[int]=Field(example=2,default=None)

class PatientCompaignPydanticModel(PatientCompaignBaseModel):
    id
    class Config:
        from_attributes=True


