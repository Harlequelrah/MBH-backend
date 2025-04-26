from pydantic import BaseModel, Field, computed_field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ..health_institution.meta_models import MetaHealthInstitutionModel


started_date_mock= datetime.now()
class CompaignBaseModel(BaseModel):
    compaign_name : str = Field(example="Summer Blood Compaign")
    compaign_type : str = Field(example="Blood Compaign")
    started_date : datetime = Field(example= started_date_mock)
    monthly_duration : int = Field(example=1)
    compaign_details : str = Field(example="The Compaign is to provide blood to lome urban children")

class CompaignCreateModel(CompaignBaseModel):
    health_institution_id : int = Field(example=1)

class CompaignUpdateModel(CompaignCreateModel):
    pass

class CompaignPatchModel(BaseModel):
    compaign_name : Optional[str] = Field(example="Summer Blood Compaign",default=None)
    compaign_type : Optional[str] = Field(example="Blood Compaign",default=None)
    start_date : datetime = Field(example= started_date_mock,default=None)
    monthly_duration : Optional[int] = Field(example=1,default=None)
    compaign_details : Optional[str] = Field(example="The Compaign is to provide blood to lome urban children",default=None)
    health_institution_id : Optional[int] = Field(example=1,default=None)



class CompaignPydanticModel(CompaignBaseModel):
    id:int
    health_institution : MetaHealthInstitutionModel

    @computed_field
    @property
    def end_date(self):
        return self.start_date  + relativedelta(months=self.monthly_duration)

    class Config:
        from_attributes=True


