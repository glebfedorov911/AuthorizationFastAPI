from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

import os
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).parent.parent

class DataBaseSettings(BaseModel):
    url: str = os.getenv("DATABASE_URL")
    echo: bool = False

class Settings(BaseModel):
    db_settings: DataBaseSettings = DataBaseSettings()

settings = Settings()