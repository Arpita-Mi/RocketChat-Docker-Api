from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    Base_Url = "http://localhost:3000/api/v1"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
