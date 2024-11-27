import jwt

from abc import ABC, abstractmethod

from app.core.config import settings

from pathlib import Path

import datetime


class AbstractTokenCreater(ABC):
    ALGORITHM: str = settings.auth_token.algorithm
    PRIVATE_KEY_PATH: str = settings.auth_token.private_key
    PUBLIC_KEY_PATH: str = settings.auth_token.public_key

    def create_token(self, payload: dict, expiration_time: int):
        expired_time = self.create_expired_time(expiration_time)
        payload = self.add_expired_time_to_payload(payload=payload, expired_date=expired_time)

        encoded = jwt.encode(payload=payload, key=self.PRIVATE_KEY_PATH, algorithm=self.ALGORITHM)
        return encoded

    @staticmethod
    def add_expired_time_to_payload(payload: dict, expired_date: datetime.datetime):
        payload.update(exp = expired_date)
        return payload

    @staticmethod
    def create_expired_time(expiration_time: int):
        return datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_time)

    def read_token(self, token: str):
        try:
            decoded = jwt.decode(jwt=token, key=self.PUBLIC_KEY_PATH, algorithms=[self.ALGORITHM])
            return decoded
        except jwt.ExpiredSignatureError:
            raise ValueError("Токен истек")
        except jwt.InvalidTokenError:
            raise ValueError("Токен не валиден")

    @abstractmethod
    def get_token(self, payload: dict):
        ...

class AccessTokenCreater(AbstractTokenCreater):
    EXPIRED_ACCESS_TOKEN: int = settings.auth_token.expired_access_token

    def get_token(self, payload: dict):
        return self.create_token(payload=payload, expiration_time=self.EXPIRED_ACCESS_TOKEN)

class RefreshTokenCreater(AbstractTokenCreater):
    EXPIRED_REFRESH_TOKEN: int = settings.auth_token.expired_refresh_token

    def get_token(self, payload: dict):
        return self.create_token(payload=payload, expiration_time=self.EXPIRED_REFRESH_TOKEN)