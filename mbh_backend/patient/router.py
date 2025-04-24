from .cruds import patient_crud
from ..settings.auth.configs import authentication
from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/patients",
    tags=["patient"],
    crud=patient_crud,
    authentication=authentication,
)

app_patient = router_provider.get_public_router()
# app_patient = router_provider.get_protected_router()

