from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+aiomysql://decion:user123@localhost/tibia_stats"
    DBBaseModel: ClassVar = declarative_base()
    JWT_SECRET: str = 'I2uUJCJ4G6Uf0Ukp_bVD_TxemExb6SLAU1dGgLHoHTw'

    class Config:
        arbitrary_types_allowed = True

    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True

settings = Settings()