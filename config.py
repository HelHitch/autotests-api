# config.py
import platform
import sys
from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    timeout: int
    url: HttpUrl

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      env_nested_delimiter=".")
    http_client: HTTPClientConfig
    test_data: TestDataConfig
    allure_results_dir: DirectoryPath
    os_info: str = f'{platform.system()}, {platform.release()}'
    python_version: str = sys.version

    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует

        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)


settings = Settings.initialize()
