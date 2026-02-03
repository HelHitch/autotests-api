from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema

public_user_client = get_public_user_client()
create_user_request = CreateUserRequestSchema(
    email="1nd3sq@bk.ru",
    password="strwewing",
    last_name="string",
    first_name="string",
    middle_name="string")
create_user_response = public_user_client.create_user(request=create_user_request)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_users_client(user=authentication_user)
user_response = private_users_client.get_user_api(user_id=create_user_response.user.id)

validate_json_schema(instance=user_response.json(),
                     schema=GetUserResponseSchema.model_json_schema())
