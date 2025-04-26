from fastapi import FastAPI
from .settings.database import engine,session_manager
from .settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from .patient.router import app_myapp as app_patient
from .settings.auth.configs import authentication_router
from .settings.auth.routers import user_router
from .health_professional.router import app_myapp as app_health_professional
from .health_institution.router import app_myapp as app_health_institution

from .institution_professional.router import app_myapp as app_institution_professional

from .campaign.router import app_myapp as app_campaign

app = FastAPI()

target_metadata.create_all(bind=engine)

# app.include_router(authentication_router)
# app.include_router(user_router)
app.include_router(app_patient)
# app.include_router(app_health_professional)
# app.include_router(app_health_institution)
# app.include_router(app_institution_professional)
# app.include_router(app_campaign)
app.add_middleware(
    ErrorHandlingMiddleware,
)

