import httpx


login_payload = {
    "email": "user@example.com",
    "password": "123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status Code:", login_response.status_code)
print("Login response:", login_response_data)


login_me = httpx.get("http://127.0.0.1:8000/api/v1/users/me",
                     headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})
print("Status Code:", login_me.status_code)
print("Login response:", login_me.json())