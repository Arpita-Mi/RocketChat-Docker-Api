from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    Base_Url = str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
