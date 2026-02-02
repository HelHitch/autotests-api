from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с пользователем без авторизации
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Выполняет POST-запрос.

        :param request: Словарь с персональными данными пользователя
        :return: Объект Response с данными ответа.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Выполняет POST-запрос.

        :param request: Словарь с персональными данными пользователя
        :return: Объект Response с данными ответа.
        """
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_user_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return PublicUsersClient(client=get_public_http_client())