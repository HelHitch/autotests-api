from pydantic import BaseModel, EmailStr, Field, constr, UUID4, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID4
    email: EmailStr = Field(..., min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(..., min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user: UserSchema