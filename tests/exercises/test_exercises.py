from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema
from fixtures.exercises import ExcerciseFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Create exercise")
    def test_create_exercise(self,
                             exercises_client: ExercisesClient):
        request = CreateExerciseRequestSchema()
        response = exercises_client.create_exercise_api(request=request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Get exercise")
    def test_get_exercise(self,
                          exercises_client: ExercisesClient,
                          function_exercise: ExcerciseFixture):
        get_exercise_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(get_exercise_response.text)
        assert_status_code(get_exercise_response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(create_exercise_response=function_exercise.response,
                                     get_exercise_response=response_data)
        validate_json_schema(get_exercise_response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Update exercise")
    def test_update_exercise(self,
                             exercises_client: ExercisesClient,
                             function_exercise: ExcerciseFixture):
        update_exercise_request = UpdateExerciseRequestSchema()
        update_exercise_response = exercises_client.update_exercise_api(request=update_exercise_request,
                                                                        exercise_id=function_exercise.response.exercise.id)
        response_data = UpdateExerciseResponseSchema.model_validate_json(update_exercise_response.text)
        assert_status_code(update_exercise_response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request=update_exercise_request, response=response_data)
        validate_json_schema(update_exercise_response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Delete exercise")
    def test_delete_exercise(self,
                             exercises_client: ExercisesClient,
                             function_exercise: ExcerciseFixture):
        delete_exercise_response = exercises_client.delete_exercise_api(
            exercise_id=function_exercise.response.exercise.id)
        assert_status_code(delete_exercise_response.status_code, HTTPStatus.OK)
        approve_delete_exercise_response = exercises_client.get_exercise_api(
            exercise_id=function_exercise.response.exercise.id)
        approve_delete_exercise_response_data = InternalErrorResponseSchema.model_validate_json(
            approve_delete_exercise_response.text)
        assert_status_code(approve_delete_exercise_response.status_code, HTTPStatus.NOT_FOUND)
        InternalErrorResponseSchema.model_validate_json(approve_delete_exercise_response.text)
        assert_exercise_not_found_response(actual=approve_delete_exercise_response_data)

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Get exercises")
    def test_get_exercises(self,
                           exercises_client: ExercisesClient,
                           function_exercise: ExcerciseFixture):
        get_exercise_query = GetExercisesQuerySchema(
            course_id=function_exercise.response.exercise.course_id
        )
        get_exercises_response = exercises_client.get_exercises_api(query=get_exercise_query)
        get_exercises_response_data = GetExercisesResponseSchema.model_validate_json(get_exercises_response.text)
        assert_status_code(get_exercises_response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(request=function_exercise.response.exercise,
                                      response=get_exercises_response_data)
