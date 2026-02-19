from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema
from fixtures.exercises import ExcerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, assert_exercise
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:

    def test_create_exercise(self,
                             exercises_client: ExercisesClient):
        request = CreateExerciseRequestSchema()
        response = exercises_client.create_exercise_api(request=request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self,
                          exercises_client: ExercisesClient,
                          function_exercise: ExcerciseFixture):
        get_exercise_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(get_exercise_response.text)
        assert_status_code(get_exercise_response.status_code, HTTPStatus.OK)
        assert_exercise(actual=function_exercise.response.exercise, expected=response_data.exercise)
        assert_get_exercise_response(request=function_exercise.request, response=response_data)
        validate_json_schema(get_exercise_response.json(), response_data.model_json_schema())
