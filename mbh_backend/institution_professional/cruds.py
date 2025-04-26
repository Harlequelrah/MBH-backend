from elrahapi.crud.crud_models import CrudModels
from .models import InstitutionProfessional  #remplacer par l'entité SQLAlchemy
from .schemas import InstitutionProfessionalCreateModel, InstitutionProfessionalUpdateModel,InstitutionProfessionalPatchModel,InstitutionProfessionalPydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager


myapp_crud_models = CrudModels(
    entity_name="institution_professional",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=InstitutionProfessional, #remplacer par l'entité SQLAlchemy
    CreateModel=InstitutionProfessionalCreateModel, #Optionel
    UpdateModel=InstitutionProfessionalUpdateModel, #Optionel
    PatchModel=InstitutionProfessionalPatchModel, #Optionel
    PydanticModel=InstitutionProfessionalPydanticModel, #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=session_manager

)
