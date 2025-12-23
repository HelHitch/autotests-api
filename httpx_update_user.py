import httpx

from tools.fakers import get_random_email

# create
create_user_payload = {
      "email": get_random_email(),
      "password": "345",
      "lastName": "345",
      "firstName": "345",
      "middleName": "123"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

print("Status Code:", create_user_response.status_code)
print("Create user response:", create_user_response_data)


# login
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status Code:", login_response.status_code)
print("Login response:", login_response_data)


# patch user
patch_payload = {
  "email": get_random_email(),
  "lastName": "345",
  "firstName": "345",
  "middleName": "345"
}

patch_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}",
                             json=patch_payload,
                             headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})
patch_response_data = login_response.json()

print("Status Code:", patch_response.status_code)
print("Patch response:", patch_response_data)