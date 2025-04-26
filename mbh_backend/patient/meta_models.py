# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
from typing import List, Optional
from .utils import BloodGroupEnum
from ..settings.auth.schemas import UserBaseModel

class PatientBaseModel(BaseModel):

    blood_group : BloodGroupEnum = Field(example=BloodGroupEnum.A_POSITIVE)
    is_blood_donor : bool = Field(example=True)


class MetaPatientModel(PatientBaseModel):
        user : UserBaseModel
