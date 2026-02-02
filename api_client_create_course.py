from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema

public_user_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email="strуreirfreer3fffng@bk.ru",
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string")


create_user_response = public_user_client.create_user(request=create_user_request)
print('Create user data ', create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(user=authentication_user)
courses_client = get_courses_client(user=authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="example.txt",
    directory="courses",
    upload_file="./testdata/test_png.jpg"
)
create_file_response = files_client.create_file(request=create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCourseRequestSchema(
    title="New Course",
    max_score=100,
    min_score=0,
    description="This is a new course.",
    estimated_time="10 hours",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id)

create_course_response = courses_client.create_course(request=create_course_request)
print("Create course data:", create_course_response)