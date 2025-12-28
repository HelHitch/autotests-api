from typing import TypedDict

from clients.api_client import APIClient


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
    courseId: int
    maxScore: int
    minScore: int
    orderIndex: int
    estimatedTime: str

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