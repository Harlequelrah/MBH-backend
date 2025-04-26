# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
from typing import List, Optional
from ..health_institution.meta_models import MetaHealthInstitutionModel
from ..health_professional.meta_models import MetaHealthProfessionalModel

class MetaIPHealthProfessionalModel(BaseModel):
    id : int
    health_professional : MetaHealthProfessionalModel

class MetaIPHealthInstitutionModel(BaseModel):
    id : int
    health_institution : MetaHealthInstitutionModel


