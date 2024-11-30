from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreateScheme

from .PasswordHasher import PasswordHasher


class RegistrationRepository:
    def __init__(self, session: AsyncSession, userIn: UserCreateScheme):
        self.session = session
        self.userIn = userIn
        self.passwordHasher = self.createPasswordHasher()

    def createPasswordHasher(self):
        password = self.userIn.password
        return PasswordHasher(password=password)

    async def createNewUser(self):
        ...

    @property
    def getHashPassword(self):
        return self.passwordHasher.hashPassword()