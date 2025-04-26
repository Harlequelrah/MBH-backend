from pydantic import BaseModel, Field,EmailStr
from typing import List, Optional
from ..institution_professional.meta_models import MetaIPHealthProfessionalModel


from .meta_models import HealthInstitutionBaseModel

from elrahapi.utility.patterns import TELEPHONE_PATTERN, URL_PATTERN
from .utils import InstitutionTypeEnum



class HealthInstitutionCreateModel(HealthInstitutionBaseModel):
    pass

class HealthInstitutionUpdateModel(HealthInstitutionBaseModel):
    pass

class HealthInstitutionPatchModel(BaseModel):
    institution_name : Optional[str] = Field(example="CHU",default=None)
    institution_email : Optional[EmailStr] = Field(example="myclinic@gmail.com",default=None)
    instution_type : Optional[InstitutionTypeEnum] = Field(example=InstitutionTypeEnum.HOSPITAL,default=None)
    institution_url: Optional[str] = Field(example="myhospital.com",default=None)
    institution_telephone: Optional[str] = Field(
        example="+22879045177",
        pattern=TELEPHONE_PATTERN
    ,default=None)
    institution_url: Optional[str] = Field(
        example="myhospital.com",
        pattern=URL_PATTERN
    ,default=None)



class HealthInstitutionPydanticModel(HealthInstitutionBaseModel):
    id : int
    health_professionals : List["MetaIPHealthProfessionalModel"] = []
    class Config:
        from_attributes=True


