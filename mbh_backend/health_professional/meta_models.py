# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
from typing import List, Optional



class HealthProfessionalBaseModel(BaseModel):
    biography: str = Field(
        example="I am a licensed physiotherapist with over 10 years of experience specializing in sports injuries and rehabilitation."
    )
    specialities : str = Field(example="physiotherapie")
    is_available : bool = Field(example = True)
class MetaHealthProfessionalModel(HealthProfessionalBaseModel):
    id : int


