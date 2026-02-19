from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    CreateCourseRequestSchema, CreateCourseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_course_response(
        request: CreateCourseRequestSchema,
        response: CreateCourseResponseSchema
):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса.

    :param request: Исходный запрос на создание курса.
    :param response: Ответ API с созданными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    if request.title is not None:
        assert_equal(response.course.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.course.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.course.min_score, request.min_score, "min_score")

    if request.description is not None:
        assert_equal(response.course.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")
