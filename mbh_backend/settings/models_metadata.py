from .database import Base
from .auth.models import metadata as user_metadata
from .logger.model import metadata as logger_metadata
from ..patient.models import metadata as myapp_metadata
from ..health_professional.models import metadata as myapp2_metadata
from ..health_institution.models import metadata as myapp3_metadata
from ..institution_professional.models import metadata as myapp4_metadata
from ..campaign.models import metadata as myapp5_metadata

from sqlalchemy import MetaData

target_metadata = MetaData()

target_metadata = Base.metadata
target_metadata = user_metadata
target_metadata = logger_metadata
target_metadata = myapp_metadata
target_metadata = myapp2_metadata
target_metadata = myapp3_metadata
target_metadata = myapp4_metadata
target_metadata = myapp5_metadata
