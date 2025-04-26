# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
from typing import List, Optional

class PatientCompaignBaseModel(BaseModel):
    patient_id:int=Field(example=1)
    compain_id:int=Field(example=2)


class MetaPatientCompaignModel(BaseModel):
    pass
