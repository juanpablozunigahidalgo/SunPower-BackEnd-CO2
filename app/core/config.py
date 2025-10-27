from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./sunpower.db"
    API_PREFIX: str = "/"
    APP_NAME: str = "SunPowerScope API"

    class Config:
        env_file = ".env"

settings = Settings()
