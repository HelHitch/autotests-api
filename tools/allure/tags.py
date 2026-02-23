from enum import Enum


class AllureTag(str, Enum):
    USERS = "users"
    FILES = "files"
    COURSES = "courses"
    EXERCISES = "exercises"
    REGRESSION = "regression"
    SMOKE = "smoke"
    AUTHENTICATION = "authentication"

    GET_ENTITY = "GET_ENTITY"
    GET_ENTITIES = "GET_ENTITIES"
    CREATE_ENTITY = "CREATE_ENTITY"
    UPDATE_ENTITY = "UPDATE_ENTITY"
    DELETE_ENTITY = "DELETE_ENTITY"
    VALIDATE_ENTITY = "VALIDATE_ENTITY"
