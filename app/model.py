from pydantic import BaseModel, Field, EmailStr

class AdvisorSchema(BaseModel):
    id: int = Field(default=None)
    name: str = Field(...)
    info: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Advisor X",
                "info": "Information for the advisor"
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Mainor Aguilar",
                "email": "mainor@savvly.com",
                "password": "password"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "mainor@savvly.com",
                "password": "password"
            }
        }
