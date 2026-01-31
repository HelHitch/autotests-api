import httpx

url = "http://127.0.0.1:8000/api/v1/users/me"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTAyLTIxVDE0OjQzOjQ5Ljk2ODIzMiIsInVzZXJfaWQiOiI1NGI3NDkxYy0zYjE1LTQxYjAtYWFjOS1iNTVlNzVlMTlhMWEifQ.597ulj6606CNAc8hH12A5TT40LpLpcJ78f6AukmotRM"
login_me = httpx.get(url, headers={"Authorization": f"Bearer {token}"})
print(login_me.json())
# login_payload = {
#     "email": "user@example.com",
#     "password": "string"
# }
#
# login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
# login_response_data = login_response.json()
#
# print("Login response:", login_response_data)
# print("Status Code:", login_response.status_code)
#
#
# refresh_payload = {
#     "refreshToken": login_response_data["token"]["refreshToken"]
# }
#
# refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
# refresh_response_data = refresh_response.json()
#
# print("Refresh response:", refresh_response_data)
# print("Status Code:", refresh_response.status_code)
