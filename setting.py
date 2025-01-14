from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BLOG_POSTGRESQL_HOST: str
    BLOG_POSTGRESQL_USER: str
    BLOG_POSTGRESQL_PORT: int = 5432
    BLOG_POSTGRESQL_PASSWORD: str
    BLOG_POSTGRESQL_DATABASE: str

    class Config:
        env_file = '.env'



def get_postgresql_setting():
    SETTINGS = Settings()

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
