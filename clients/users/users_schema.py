from pydantic import BaseModel, constr, Field, ConfigDict, EmailStr

from tools import fake


class CreateUserRequestSchema(BaseModel):
    """Схема на создание пользователя."""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: constr(min_length=1, max_length=50) = Field(default_factory=fake.last_name, alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(default_factory=fake.first_name, alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(default_factory=fake.middle_name, alias="middleName")


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
    last_name: constr(min_length=1, max_length=50) | None = Field(default_factory=fake.last_name, alias="lastName")
    first_name: constr(min_length=1, max_length=50) | None = Field(default_factory=fake.first_name(), alias="firstName")
    middle_name: constr(min_length=1, max_length=50) | None = Field(default_factory=fake.middle_name(),
                                                                    alias="middleName")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении пользователя.
    """
    user: UserSchema
