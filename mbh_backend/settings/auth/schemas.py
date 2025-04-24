from typing import List, Optional
from elrahapi.user import  schemas
from pydantic import Field,BaseModel
from .enums import SexEnum


class UserBaseModel(BaseModel,schemas.UserBaseModel):
    address : str = Field(example="Lomé,Togo")
    telephone: str = Field(
        example="+22891361029",
        pattern=r"^\+\d{8,15}$",
        description="Telephone number must be in the format +<country_code><number>"
    )
    sex : SexEnum = Field(example=SexEnum.MALE)

class UserCreateModel(UserBaseModel, schemas.UserCreateModel):
    pass

class UserUpdateModel(UserBaseModel,schemas.UserUpdateModel):
    pass



class UserPatchModel(BaseModel,schemas.UserPatchModel):
    address : Optional[str] = Field(example="Lomé,Togo",default=None)
    telephone: Optional[str] = Field(
        example="+22891361029",
        pattern=r"^\+\d{8,15}$",
        description="Telephone number must be in the format +<country_code><number>",
        default=None
    )
    sex : Optional[SexEnum] = Field(example=SexEnum.MALE,default=None)

class UserPydanticModel(UserBaseModel,schemas.UserPydanticModel):
    class Config :
        from_attributes=True



