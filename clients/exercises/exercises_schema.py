from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(..., alias="courseId")
    max_score: int = Field(..., alias="maxScore")
    min_score: int = Field(..., alias="minScore")
    order_index: int = Field(..., alias="orderIndex")
    estimated_time: str = Field(..., alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(..., alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(..., alias="courseId")
    max_score: int = Field(..., alias="maxScore")
    min_score: int = Field(..., alias="minScore")
    order_index: int = Field(..., alias="orderIndex")
    estimated_time: str = Field(..., alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    course_id: str = Field(..., alias="courseId")
    max_score: int = Field(..., alias="maxScore")
    min_score: int = Field(..., alias="minScore")
    order_index: int = Field(..., alias="orderIndex")
    estimated_time: str = Field(..., alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    exercises: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении списка заданий.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении задания.
    """
    exercise: ExerciseSchema
