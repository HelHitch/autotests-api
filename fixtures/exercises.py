import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from fixtures.users import UserFixture


class ExcercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(user=function_user.authentication_user)


@pytest.fixture
def function_exercise(exercises_client: ExercisesClient) -> ExcercisesFixture:
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request=request)
    return ExcercisesFixture(request=request, response=response)
