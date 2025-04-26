# This file can be used to create utilities for the application
import enum

class InstitutionTypeEnum(enum.Enum):
    HOSPITAL = "Hôpital"
    CLINIC = "Clinique"
    ONG = "ONG"
    STARTUP = "Startup"
    CABINET = "Cabinet"
    PMI = "Protection Maternelle et Infantile"
    PRIVATE = "Privée"
