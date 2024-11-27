from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

import os
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).parent.parent
CERTS_DIR = "core/certs"

class DataBaseSettings(BaseModel):
    url: str = os.getenv("DATABASE_URL")
    echo: bool = False

class AuthorizationToken(BaseModel):

    algorithm: str = os.getenv("ALGORITHM")
    private_key: Path = (BASE_DIR / CERTS_DIR / os.getenv("PRIVATE_KEY_PATH")).read_text()
    public_key: Path = (BASE_DIR / CERTS_DIR / os.getenv("PUBLIC_KEY_PATH")).read_text()
    expired_access_token: int = int(os.getenv("EXPIRED_ACCESS_TOKEN"))
    expired_refresh_token: int = int(os.getenv("EXPIRED_REFRESH_TOKEN"))

class Settings(BaseModel):
    db_settings: DataBaseSettings = DataBaseSettings()
    auth_token: AuthorizationToken = AuthorizationToken()

settings = Settings()