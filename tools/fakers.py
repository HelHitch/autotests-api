import time

from faker import Faker


def get_random_email() -> str:
    """
    Генерирует случайный адрес электронной почты.

    Возвращает:
        str: Случайный адрес электронной почты в формате test.<timestamp>@example.com.
    """
    return f"test.{time.time()}@example.com"


class Fake:
    """
    Класс-обертка для генерации фейковых данных с использованием библиотеки Faker.

    Атрибуты:
        faker (Faker): Экземпляр класса Faker для генерации данных.
    """

    def __init__(self, faker: Faker):
        """
        Инициализирует объект Fake.

        Аргументы:
            faker (Faker): Экземпляр класса Faker.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст.

        Возвращает:
            str: Случайный текст.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4.

        Возвращает:
            str: Случайный UUID4.
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        Возвращает:
            str: Случайное предложение.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        Возвращает:
            str: Случайный пароль.
        """
        return self.faker.password()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        Возвращает:
            str: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество.

        Возвращает:
            str: Случайное отчество.
        """
        return self.faker.middle_name()

    def last_name(self) -> str:
        """
        Генерирует случайное отчество.

        Возвращает:
            str: Случайное отчество.
        """
        return self.faker.last_name()

    def time(self) -> str:
        """
        Генерирует случайное время.

        Возвращает:
            str: Случайное время.
        """
        return self.faker.time()

    def estimated_time(self) -> str:
        """
        Генерирует случайное значение предполагаемого времени выполнения.

        Возвращает:
            str: Случайное значение времени в неделях.
        """
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        """
        Генерирует случайное максимальное значение оценки.

        Возвращает:
            int: Случайное значение от 50 до 100.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайное минимальное значение оценки.

        Возвращает:
            int: Случайное значение от 1 до 30.
        """
        return self.integer(1, 30)

    def integer(self, min: int, max: int) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        Аргументы:
            min (int): Минимальное значение.
            max (int): Максимальное значение.

        Возвращает:
            int: Случайное целое число в диапазоне [min, max].
        """
        return self.faker.random_int(min=min, max=max)


fake = Fake(faker=Faker('ru_RU'))
