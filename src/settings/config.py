from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    schiphol_app_id: str = "c7c99d11"
    schiphol_api_key: str = "d9cee2d3793757d9ec8b1609aecf0147"
    schiphol_base_url: str = "https://api.schiphol.nl/"
