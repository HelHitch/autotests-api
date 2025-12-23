from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


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
