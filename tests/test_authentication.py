from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code


@pytest.mark.authentication
@pytest.mark.regression
def test_login(function_user: UserFixture,
               authentication_client: AuthenticationClient):
    authentication_user = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )
    auth_client_response = authentication_client.login_api(authentication_user)
    login_response_data = LoginResponseSchema.model_validate_json(auth_client_response.text)

    assert_status_code(actual=auth_client_response.status_code,
                       expected=HTTPStatus.OK)
    assert_login_response(response=login_response_data)
