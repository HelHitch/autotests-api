from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema):
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

    def create_exercise_api(self, request: CreateExerciseRequestSchema):
        """
        Метод для создания задания

        :param request: Словарь со списком полей для создания курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema):
        """
        Метод обновления задачния

        :param exercise_id: Идентификатор задания
        :param request: Словарь со списком полей для обновления курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}",
                          json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str):
        """
        Метод удаления задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения одного задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод получения списка заданий курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercises_api(query=query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод для создания задания

        :param request: Словарь со списком полей для создания курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод обновления задачния

        :param exercise_id: Идентификатор задания
        :param request: Словарь со списком полей для обновления курса"""
        response = self.update_exercise_api(exercise_id=exercise_id,
                                            request=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Фабричная функция для получения клиента заданий.

    :return: Экземпляр ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user=user))