from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Login with correct login and password")
    def test_login(self, function_user: UserFixture,
                   authentication_client: AuthenticationClient):
        authentication_user = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        auth_client_response = authentication_client.login_api(authentication_user)
        login_response_data = LoginResponseSchema.model_validate_json(auth_client_response.text)

        assert_status_code(actual=auth_client_response.status_code,
                           expected=HTTPStatus.OK)
        assert_login_response(response=login_response_data)
