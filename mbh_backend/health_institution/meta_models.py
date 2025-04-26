# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

from elrahapi.utility.patterns import TELEPHONE_PATTERN, URL_PATTERN
from .utils import InstitutionTypeEnum



class HealthInstitutionBaseModel(BaseModel):
    institution_name : str = Field(example="CHU")
    institution_email : EmailStr = Field(example="myclinic@gmail.com")
    instution_type : InstitutionTypeEnum = Field(example=InstitutionTypeEnum.HOSPITAL)
    institution_url: str = Field(example="myhospital.com")
    institution_telephone: str = Field(
        example="+22879045177",
        pattern=TELEPHONE_PATTERN
    )
    institution_url: str = Field(
        example="myhospital.com",
        pattern=URL_PATTERN
    )

class MetaHealthInstitutionModel(HealthInstitutionBaseModel):
    id : int
