from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar
from sqlalchemy.orm.decl_api import DeclarativeMeta
import secrets

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://Thiago:1234@localhost:5432/Faculdade'
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    
    JWT_SECRET: str = '' # Aqui nos vamos colocar uma string aleatoria, para ser o segredo do JWT
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    
    
    class Config:
        case_sensitive = True

settings = Settings()
token = secrets.token_urlsafe(32)
settings.JWT_SECRET = token

with open('token.txt', 'w') as f:
    f.write(token)
