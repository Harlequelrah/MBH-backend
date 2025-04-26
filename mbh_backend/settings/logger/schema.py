from elrahapi.middleware.models import LoggerMiddlewareReadModel
class LogPydanticModel(LoggerMiddlewareReadModel):
    class setting:
        from_attributes=True



