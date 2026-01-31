from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_user_client, CreateRequestDict

public_user_client = get_public_user_client()

create_user_request = CreateRequestDict(
    email="str4iffn4g@bk.ru",
    password="string",
    lastName="string",
    firstName="string",
    middleName="string")


create_user_response = public_user_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(user=authentication_user)
courses_client = get_courses_client(user=authentication_user)

create_file_request = CreateFileRequestDict(
    filename="example.txt",
    directory="courses",
    upload_file="./testdata/test_png.jpg"
)
create_file_response = files_client.create_file(request=create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCourseRequestDict(
    title="New Course",
    maxScore=100,
    minScore=0,
    description="This is a new course.",
    estimatedTime="10 hours",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id'])

create_course_response = courses_client.create_course(request=create_course_request)
print("Create course data:", create_course_response)