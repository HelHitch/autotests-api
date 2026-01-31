from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import CreateRequestDict, get_public_user_client

public_user_client = get_public_user_client()

create_user_request = CreateRequestDict(
    email="striffng@bk.ru",
    password="string",
    lastName="string",
    firstName="string",
    middleName="string")


create_user_response = public_user_client.create_user(request=create_user_request)
print('Create user data ', create_user_response)

auth_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
private_users_client = get_private_users_client(user=auth_user)
get_user_response = private_users_client.get_user_api(user_id=create_user_response['user_id'])
get_user_response_data = get_user_response.json()
print('Get user data ', get_user_response_data)