from fastapi import FastAPI
from .settings.database import engine,session_manager
from .settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from .patient.router import app_patient
from .settings.auth.configs import authentication_router
from .settings.auth.routers import user_router
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(user_router)
app.include_router(app_patient)
app.include_router(authentication_router)
app.add_middleware(
    ErrorHandlingMiddleware,
)

