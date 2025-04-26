from elrahapi.crud.crud_models import CrudModels
from .models import HealthProfessional  #remplacer par l'entité SQLAlchemy
from .schemas import HealthProfessionalCreateModel, HealthProfessionalUpdateModel,HealthProfessionalPatchModel,HealthProfessionalPydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager


myapp_crud_models = CrudModels(
    entity_name="health_professional",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=HealthProfessional, #remplacer par l'entité SQLAlchemy
    CreateModel=HealthProfessionalCreateModel, #Optionel
    UpdateModel=HealthProfessionalUpdateModel, #Optionel
    PatchModel=HealthProfessionalPatchModel, #Optionel
    PydanticModel=HealthProfessionalPydanticModel, #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=session_manager
)
