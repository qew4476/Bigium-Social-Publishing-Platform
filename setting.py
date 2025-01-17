from pydantic_settings import BaseSettings, SettingsConfigDict
import os

STAGE = os.getenv('STAGE')


class Settings(BaseSettings):
    BLOG_POSTGRESQL_HOST: str
    BLOG_POSTGRESQL_USER: str
    BLOG_POSTGRESQL_PORT: int = 5432
    BLOG_POSTGRESQL_PASSWORD: str
    BLOG_POSTGRESQL_DATABASE: str
    STAGE: str
    model_config = SettingsConfigDict(env_file=f'{STAGE}.config.env', env_file_encoding='utf-8')


def get_postgresql_setting():
    SETTINGS = Settings()
    print(SETTINGS)
    return {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": SETTINGS.BLOG_POSTGRESQL_DATABASE,
            "USER": SETTINGS.BLOG_POSTGRESQL_USER,
            "PASSWORD": SETTINGS.BLOG_POSTGRESQL_PASSWORD,
            "HOST": SETTINGS.BLOG_POSTGRESQL_HOST,
            "PORT": SETTINGS.BLOG_POSTGRESQL_PORT
        }
    }
