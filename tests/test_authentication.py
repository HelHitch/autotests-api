from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code


def test_login():
    public_user_client = get_public_user_client()

    create_user_request_schema = CreateUserRequestSchema()
    public_user_client.create_user(create_user_request_schema)
    authentication_user = LoginRequestSchema(
        email=create_user_request_schema.email,
        password=create_user_request_schema.password
    )

    auth_client = get_authentication_client()
    auth_client_response = auth_client.login_api(authentication_user)
    login_response_data = LoginResponseSchema.model_validate_json(auth_client_response.text)

    assert_status_code(actual=auth_client_response.status_code,
                       expected=HTTPStatus.OK)
    assert_login_response(response=login_response_data)
