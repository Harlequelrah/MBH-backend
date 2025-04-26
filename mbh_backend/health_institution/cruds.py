from elrahapi.crud.crud_models import CrudModels
from .models import HealthInstitution  #remplacer par l'entité SQLAlchemy
from .schemas import HealthInstitutionCreateModel, HealthInstitutionUpdateModel,HealthInstitutionPatchModel,HealthInstitutionPydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager


myapp_crud_models = CrudModels(
    entity_name="health_institution",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=HealthInstitution, #remplacer par l'entité SQLAlchemy
    CreateModel=HealthInstitutionCreateModel, #Optionel
    UpdateModel=HealthInstitutionUpdateModel, #Optionel
    PatchModel=HealthInstitutionPatchModel, #Optionel
    PydanticModel=HealthInstitutionPydanticModel, #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=session_manager

)
