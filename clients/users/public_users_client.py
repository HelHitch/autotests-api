from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict
from clients.public_http_builder import get_public_http_client


class CreateRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    id: str
    email:str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с пользователем без авторизации
    """

    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
        Выполняет POST-запрос.

        :param request: Словарь с персональными данными пользователя
        :return: Объект Response с данными ответа.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateRequestDict) -> CreateUserResponseDict:
        """
        Выполняет POST-запрос.

        :param request: Словарь с персональными данными пользователя
        :return: Объект Response с данными ответа.
        """
        response = self.create_user_api(request=request)
        return response.json()

def get_public_user_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return PublicUsersClient(client=get_public_http_client())