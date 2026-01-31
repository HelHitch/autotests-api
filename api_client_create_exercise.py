
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_user_client, CreateRequestDict

public_user_client = get_public_user_client()

create_user_request = CreateRequestDict(
    email="test_look_@bk.ru",
    password="string",
    lastName="string",
    firstName="string",
    middleName="string")

new_user = public_user_client.create_user(request=create_user_request)
print("Create user data:", new_user)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)


create_file_request = CreateFileRequestDict(
    filename="example.txt",
    directory="courses",
    upload_file="./testdata/test_png.jpg"
)
files_client = get_files_client(user=authentication_user)
create_file_response = files_client.create_file(request=create_file_request)
print("Create file data:", create_file_response)


courses_client = get_courses_client(user=authentication_user)
create_course_request = CreateCourseRequestDict(
    title="New Course",
    maxScore=100,
    minScore=0,
    description="This is a new course.",
    estimatedTime="10 hours",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=new_user['user']['id'])

create_course_response = courses_client.create_course(request=create_course_request)
print("Create course data:", create_course_response)

exercises_client = get_exercises_client(user=authentication_user)
create_exercise_request = CreateExerciseRequestDict(
    title="New Exercise",
    courseId=create_course_response['course']['id'],
    maxScore=50,
    minScore=0,
    orderIndex=1,
    estimatedTime="2 hours")
create_exercise_response = exercises_client.create_exercise(request=create_exercise_request)
print("Create exercise data:", create_exercise_response)