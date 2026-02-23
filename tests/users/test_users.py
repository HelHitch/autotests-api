from http import HTTPStatus

import allure
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools import fake
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, public_users_client: PublicUsersClient, email: str):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа создания юзера
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @pytest.mark.users
    @pytest.mark.regression
    @allure.title("Get user me")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    def test_get_user_me(self, function_user: UserFixture,
                         authentication_client: AuthenticationClient,
                         private_users_client: PrivateUsersClient):
        authentication_user = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        authentication_client.login_api(authentication_user)
        response = private_users_client.get_user_me_api()
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        response_user_model = GetUserResponseSchema.model_validate_json(response.text)
        validate_json_schema(instance=response.json(),
                             schema=response_user_model.model_json_schema())
        assert_get_user_response(get_user_response=response_user_model,
                                 create_user_response=function_user.response)
