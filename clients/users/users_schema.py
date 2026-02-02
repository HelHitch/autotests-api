from pydantic import BaseModel, constr, Field, ConfigDict, EmailStr


class CreateUserRequestSchema(BaseModel):
    """Схема на создание пользователя."""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class UserSchema(BaseModel):
    """Схема пользователя."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: constr(min_length=1, max_length=50) | None = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) | None = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) | None = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении пользователя.
    """
    user: UserSchema
