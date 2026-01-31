from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client



class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: int
    maxScore: int
    minScore: int
    orderIndex: int
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    courseId: int | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    exercises: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при получении списка заданий.
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при получении задания.
    """
    exercise: Exercise

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict):
        """
        Метод получения списка заданий курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str):
        """
        Метод получения одного задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict):
        """
        Метод для создания задания

        :param request: Словарь со списком полей для создания курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request:UpdateExerciseRequestDict):
        """
        Метод обновления задачния

        :param exercise_id: Идентификатор задания
        :param request: Словарь со списком полей для обновления курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}",
                          json=request)

    def delete_exercise_api(self, exercise_id: str):
        """
        Метод удаления задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения одного задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения списка заданий курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercises_api(query=query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод для создания задания

        :param request: Словарь со списком полей для создания курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request:UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления задачния

        :param exercise_id: Идентификатор задания
        :param request: Словарь со списком полей для обновления курса"""
        response = self.update_exercise_api(exercise_id=exercise_id,
                                            request=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Фабричная функция для получения клиента заданий.

    :return: Экземпляр ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user=user))