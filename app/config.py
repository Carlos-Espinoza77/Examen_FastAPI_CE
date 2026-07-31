from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_description: str
    app_version: str

    debug: bool

    secret_key: str

    database_url: str