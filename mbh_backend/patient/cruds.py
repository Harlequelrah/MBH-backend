from elrahapi.crud.crud_models import CrudModels
from .models import Patient  #remplacer par l'entité SQLAlchemy
from .schemas import PatientCreateModel, PatientUpdateModel,PatientPatchModel,PatientPydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager


myapp_crud_models = CrudModels(
    entity_name="patient",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Patient, #remplacer par l'entité SQLAlchemy
    CreateModel=PatientCreateModel, #Optionel
    UpdateModel=PatientUpdateModel, #Optionel
    PatchModel=PatientPatchModel, #Optionel
    PydanticModel=PatientPydanticModel, #Optionel
)
patient_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=session_manager

)
