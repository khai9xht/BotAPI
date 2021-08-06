from pydantic import BaseSettings


class Settings(BaseSettings):
	SERVER_HOST: str = "0.0.0.0"
	SERVER_PORT: int = 6789
	database_url: str = "sqlite://college.db"
	
settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)