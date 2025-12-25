# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "PatentAI Projesi"
    API_V1_STR: str = "/api/v1"

    # Bu ayar, .env dosyasından ayarları okumayı sağlar (ileride kullanacağız)
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()