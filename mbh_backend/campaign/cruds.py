from elrahapi.crud.crud_models import CrudModels
from .models import Compaign  #remplacer par l'entité SQLAlchemy
from .schemas import CompaignCreateModel, CompaignUpdateModel,CompaignPatchModel,CompaignPydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager


myapp_crud_models = CrudModels(
    entity_name="compaign",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Compaign, #remplacer par l'entité SQLAlchemy
    CreateModel=CompaignCreateModel, #Optionel
    UpdateModel=CompaignUpdateModel, #Optionel
    PatchModel=CompaignPatchModel, #Optionel
    PydanticModel=CompaignPydanticModel, #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=session_manager

)
